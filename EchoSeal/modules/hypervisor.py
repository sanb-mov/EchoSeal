import time
import os
from utils.logger import log

def check_hypervisor():
    score = 0
    log("Analizando Hipervisor y Timing...", "HEADER")

    # 1. Timing Attack (RDTSC simulation)
    # Las VMs tardan más en ejecutar ciertas instrucciones debido al overhead del hipervisor
    start = time.perf_counter()
    for i in range(1000000):
        pass # Loop vacío
    end = time.perf_counter()
    diff = end - start
    
    log(f"Latencia de bucle simple: {diff:.6f}s")
    
    # Umbral empírico (ajustar según pruebas)
    if diff > 0.15: 
        log("Latencia de CPU inusualmente alta (Posible emulación)", "WARN")
        score += 20

    # 2. Comprobar archivos de dispositivos especiales (Linux) o claves de registro (Windows)
    # Simulación básica multiplataforma
    known_vm_files = [
        "/proc/vz", "/proc/bc", "/proc/xen", # Linux
        "C:\\windows\\system32\\drivers\\vboxmouse.sys", # Windows VBox
        "C:\\windows\\system32\\drivers\\vmhgfs.sys" # Windows VMware
    ]

    found_files = 0
    for f in known_vm_files:
        if os.path.exists(f):
            log(f"Artefacto de hipervisor encontrado: {f}", "ALERT")
            found_files += 1
            
    if found_files > 0:
        score += 40

    return score