import psutil
import uuid
import platform
from utils.logger import log

def check_hardware():
    score = 0
    log("Analizando Hardware...", "HEADER")

    # 1. Verificar Núcleos de CPU
    cores = psutil.cpu_count(logical=False)
    log(f"Núcleos Físicos detectados: {cores}")
    if cores < 2:
        log("Detectado 1 solo núcleo (Común en Sandboxes básicas)", "WARN")
        score += 20
    
    # 2. Verificar RAM (Las VMs suelen tener RAM exacta, ej: 4096MB, las PC reales no)
    mem = psutil.virtual_memory()
    total_gb = mem.total / (1024**3)
    log(f"Memoria RAM Total: {total_gb:.2f} GB")
    
    if mem.total < 2 * 1024**3: # Menos de 2GB
        log("Memoria sospechosamente baja (< 2GB)", "WARN")
        score += 15

    # 3. MAC Address Spoofing / Vendors Virtuales
    mac_num = hex(uuid.getnode()).replace('0x', '').upper()
    mac = ':'.join(mac_num[i : i + 2] for i in range(0, 11, 2))
    log(f"MAC Address: {mac}")
    
    virtual_prefixes = [
        "00:05:69", "00:0C:29", "00:1C:14", "00:50:56", # VMware
        "00:03:FF", # Hyper-V
        "08:00:27"  # VirtualBox
    ]
    
    for prefix in virtual_prefixes:
        if mac.startswith(prefix):
            log(f"MAC Address corresponde a virtualización conocida: {prefix}", "ALERT")
            score += 50
            break

    return score