import sys
import os
import time
from utils.logger import log, Colors
from modules import hardware, hypervisor, filesystem, behavior, kernel

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{Colors.HEADER}
    ███████╗ ██████╗██╗  ██╗ ██████╗ ███████╗███████╗ █████╗ ██╗
    ██╔════╝██╔════╝██║  ██║██╔═══██╗██╔════╝██╔════╝██╔══██╗██║
    █████╗  ██║     ███████║██║   ██║███████╗█████╗  ███████║██║
    ██╔══╝  ██║     ██╔══██║██║   ██║╚════██║██╔══╝  ██╔══██║██║
    ███████╗╚██████╗██║  ██║╚██████╔╝███████║███████╗██║  ██║███████╗
    ╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝
            -- Detección de Manipulación de Entornos --
    {Colors.RESET}""")

    log("Iniciando EchoSeal v1.0...", "INFO")
    
    total_score = 0
    
    # Ejecutar módulos
    try:
        total_score += hardware.check_hardware()
        total_score += hypervisor.check_hypervisor()
        total_score += filesystem.check_filesystem()
        total_score += kernel.check_kernel()
        total_score += behavior.check_behavior()
    except Exception as e:
        log(f"Error crítico durante el análisis: {e}", "FAIL")

    print("\n" + "="*50)
    log(f"PUNTUACIÓN DE MANIPULACIÓN: {total_score}/100", "HEADER")
    
    if total_score == 0:
        print(f"{Colors.OK}RESULTADO: Entorno Limpio (Bare Metal real).{Colors.RESET}")
    elif total_score < 50:
        print(f"{Colors.WARN}RESULTADO: Entorno Sospechoso (Posibles artefactos residuales).{Colors.RESET}")
    else:
        print(f"{Colors.FAIL}RESULTADO: ALTA PROBABILIDAD DE ENTORNO VIRTUAL/MANIPULADO.{Colors.RESET}")
        print(f"{Colors.FAIL}⚠ Este sistema parece ser un Sandbox, VM o ha sido hookeado. ⚠{Colors.RESET}")
    
    print("="*50)
    input("\nPresiona Enter para salir...")

if __name__ == "__main__":
    # Se requieren permisos de administrador para ver drivers y ciertos metadatos
    try:
        main()
    except KeyboardInterrupt:
        print("\nSaliendo...")