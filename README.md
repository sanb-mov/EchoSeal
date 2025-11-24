# 🔍EchoSeal
### Advanced Virtual Environment & Sandbox Manipulation Detector

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey) ![License](https://img.shields.io/badge/License-MIT-green) ![Status](https://img.shields.io/badge/Status-Beta-orange)

**EchoSeal** es una herramienta open-source de contra-inteligencia diseñada para detectar si el sistema operativo actual está siendo ejecutado dentro de un entorno virtualizado, un sandbox de análisis de malware o si ha sido manipulado para ocultar su naturaleza virtual.

A diferencia de las herramientas tradicionales que buscan malware, **EchoSeal audita el propio entorno** para asegurar que sea un hardware real ("Bare Metal") y no una simulación controlada por atacantes o analistas.

---

## ⚠️ ¿Qué problema resuelve?

Muchos atacantes y malware modernos ("evasive malware") detectan si están en una máquina virtual (VirtualBox, VMware, Cuckoo Sandbox) y detienen su actividad para evitar ser analizados.
**EchoSeal hace lo contrario:** Permite a los administradores y Red Teamers verificar si un entorno ha sido adulterado para parecer una máquina real cuando no lo es.

### Capacidades Principales

🔍 **1. Análisis de Hardware (Hardware Fingerprinting)**
*   Detección de núcleos de CPU inconsistentes (ej. 1 solo núcleo).
*   Verificación de RAM con tamaños "demasiado perfectos" (típico de asignación VM).
*   Detección de MAC Address Spoofing y prefijos de vendors virtuales (VMware, Hyper-V, Xen).

⏱️ **2. Análisis de Hipervisor & Timing (Timing Attacks)**
*   Ejecución de pruebas de latencia de CPU (RDTSC checks).
*   Detección de discrepancias de tiempo causadas por la sobrecarga del hipervisor (instrucciones `CPUID`).
*   Búsqueda de artefactos de "Backdoor I/O ports".

🧠 **3. Análisis Conductual (Dynamic Behavior)**
*   **Sleep Patching Detection:** Detecta si el sistema está "acelerando el tiempo" para saltarse las esperas (`time.sleep`), una técnica común en sandboxes automatizados.

📂 **4. Inconsistencias del Filesystem**
*   Detección de drivers y archivos fantasma específicos de virtualización.
*   Análisis de **Timestomping**: Archivos de sistema con fechas de modificación anteriores a su creación.
*   Verificación de tamaño de disco inusualmente pequeño.

⚙️ **5. Inspección de Kernel (User-Mode)**
*   Enumeración de drivers cargados para detectar herramientas de guest additions.
*   (Experimental) Detección de hooks básicos en APIs de Windows.

---
