import time
from utils.logger import log

def check_behavior():
    score = 0
    log("Analizando Comportamiento Dinámico...", "HEADER")

    # 1. Sleep Patching Check
    requested_sleep = 2.0
    start = time.time()
    time.sleep(requested_sleep)
    end = time.time()
    elapsed = end - start
    
    log(f"Sleep solicitado: {requested_sleep}s | Real: {elapsed:.4f}s")
    
    # Si la diferencia es negativa significativa o muy pequeña (aceleración de tiempo)
    if elapsed < (requested_sleep - 0.2):
        log("DETECTADA ACELERACIÓN DE TIEMPO (Sandbox Environment)", "ALERT")
        score += 100  # Detección casi segura
    
    # 2. Detección de interacción de usuario (Mouse)
    # En entornos automatizados, el mouse a veces salta o no se mueve.
    # Requiere librerías gráficas, omitido para mantenerlo CLI puro, 
    # pero podríamos verificar la posición del cursor via ctypes.

    return score