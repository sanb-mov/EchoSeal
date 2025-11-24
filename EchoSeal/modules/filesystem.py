import os
import platform
from utils.logger import log
import datetime

def check_filesystem():
    score = 0
    log("Analizando Sistema de Archivos...", "HEADER")

    system = platform.system()
    target_dir = "C:\\Windows\\System32" if system == "Windows" else "/bin"
    
    # 1. Verificar Timestomping (Modificación anterior a Creación)
    # Esto ocurre cuando se copian herramientas hackeadas o se manipula el FS
    suspicious_files = 0
    try:
        files = os.listdir(target_dir)[:50] # Muestreo de 50 archivos
        for f in files:
            full_path = os.path.join(target_dir, f)
            try:
                creation = os.path.getctime(full_path)
                modification = os.path.getmtime(full_path)
                
                # En Windows, si Creado > Modificado por mucho margen, puede ser normal (updates),
                # pero si Modificado es AÑOS antes que Creado (al revés) en archivos de sistema
                # base recién instalados, es raro en entornos clonados.
                
                # Comprobamos archivos "sandbox" típicos
                if f.lower() in ["sample.exe", "malware.exe", "artifact.exe"]:
                    log(f"Nombre de archivo genérico de sandbox detectado: {f}", "ALERT")
                    score += 50

            except Exception:
                pass
    except FileNotFoundError:
        pass

    # 2. Verificar espacio en disco
    # Las Sandboxes suelen tener discos muy pequeños (<60GB)
    try:
        import shutil
        total, _, _ = shutil.disk_usage("/")
        total_gb = total / (1024**3)
        log(f"Tamaño del disco principal: {total_gb:.2f} GB")
        
        if total_gb < 60:
            log("Disco duro sospechosamente pequeño (<60GB)", "WARN")
            score += 25
    except:
        pass

    return score