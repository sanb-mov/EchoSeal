import sys
import platform
from utils.logger import log

def check_kernel():
    score = 0
    log("Analizando Kernel y Drivers...", "HEADER")
    
    if platform.system() != "Windows":
        log("Análisis profundo de kernel limitado a Windows en esta versión.", "WARN")
        return 0

    import ctypes
    from ctypes import wintypes

    # Definiciones para API de Windows
    psapi = ctypes.WinDLL('psapi.dll')
    kernel32 = ctypes.WinDLL('kernel32.dll')
    
    ARRAY_SIZE = 1024
    lpImageBase = (ctypes.c_void_p * ARRAY_SIZE)()
    cbNeeded = ctypes.c_ulong()
    
    # Obtener lista de direcciones base de drivers
    if psapi.EnumDeviceDrivers(ctypes.byref(lpImageBase), ctypes.sizeof(lpImageBase), ctypes.byref(cbNeeded)):
        drivers_count = cbNeeded.value // ctypes.sizeof(ctypes.c_void_p)
        log(f"Drivers cargados en kernel: {drivers_count}")
        
        suspicious_drivers = ["vbox", "vmware", "xen", "virtio", "sandbox"]
        found_suspicious = False
        
        szDriver = ctypes.create_string_buffer(250)
        
        for i in range(drivers_count):
            psapi.GetDeviceDriverBaseNameA(lpImageBase[i], szDriver, ctypes.sizeof(szDriver))
            driver_name = szDriver.value.decode("utf-8", errors="ignore").lower()
            
            for susp in suspicious_drivers:
                if susp in driver_name:
                    log(f"Driver sospechoso detectado: {driver_name}", "ALERT")
                    found_suspicious = True
                    score += 20
    else:
        log("No se pudo enumerar los drivers (¿Faltan permisos de Admin?)", "FAIL")
        
    return score