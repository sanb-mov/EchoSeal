
## 🔨 Guía de Compilación de EchoSeal

Esta guía detalla los pasos para convertir el código fuente Python de **EchoSeal** en un ejecutable binario (`.exe` para Windows o binario ELF para Linux) que funcione de manera autónoma (portable), sin necesidad de instalar Python en la máquina objetivo.

---

## 📋 1. Prerrequisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu sistema:
```
1.  Python 3.8 o superior: [Descargar Python](https://www.python.org/downloads/).
Nota:* Al instalar en Windows, asegúrate de marcar la casilla **"Add Python to PATH"**.
2.  **Git** (Opcional, para clonar el repo).
```
---

## ⚙️ 2. Preparación del Entorno

Se recomienda usar un entorno virtual para evitar conflictos con otras librerías de tu sistema.

### Paso 2.1: Crear entorno virtual (Opcional pero recomendado)
```
**En Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**En Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Paso 2.2: Instalar dependencias

Instala las librerías necesarias definidas en el proyecto, incluyendo `pyinstaller` (el compilador).

```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install pyinstaller
```

---

## 🚀 3. Proceso de Compilación (Build)

Una vez instaladas las dependencias, ejecutaremos **PyInstaller**. Este comando empaqueta el intérprete de Python, las librerías y tus scripts en un solo archivo.

### Comando de Compilación

Abre tu terminal en la carpeta raíz del proyecto y ejecuta:

```bash
python -m PyInstaller --onefile --clean --name=EchoSeal main.py
```

### 🧩 Desglose del comando:
*   `python -m PyInstaller`: Ejecuta el módulo de compilación.
*   `--onefile`: Crea **un único archivo** `.exe` (en lugar de una carpeta con cientos de archivos sueltos).
*   `--clean`: Limpia la caché de compilaciones anteriores para evitar errores.
*   `--name=EchoSeal`: Nombra el archivo final como `EchoSeal.exe`.
*   `main.py`: Es el script principal que inicia el programa.

---

## ⚠️ 4. Solución de Problemas Comunes

### 🛡️ Error: "FileNotFoundError" o el archivo desaparece
Si la compilación termina pero no encuentras el archivo `.exe`, o recibes un error de "Access Denied" / "File not found" al final del proceso.

**Causa:**
Tu Antivirus (Windows Defender, Avast, etc.) ha detectado que EchoSeal intenta analizar el hardware y hooks del sistema. Al ser una herramienta de seguridad ofensiva/defensiva, **se clasifica como un "Falso Positivo" y es eliminado instantáneamente**.

**Solución:**
1.  **Desactiva temporalmente la "Protección en tiempo real"** de tu antivirus antes de compilar.
2.  Ejecuta el comando de compilación nuevamente.
3.  Crea una **Exclusión** en tu antivirus para la carpeta `dist/` o para el archivo `EchoSeal.exe`.
4.  Vuelve a activar tu antivirus.

### ❌ Error: "No module named..."
Si la compilación falla diciendo que falta un módulo (ej. `ModuleNotFoundError: No module named 'psutil'`).

**Solución:**
Asegúrate de haber instalado las dependencias **en el mismo entorno** donde estás ejecutando PyInstaller:
```bash
pip install -r requirements.txt
```

---

## 📦 5. Localizar el Ejecutable

Si todo ha salido bien, verás un mensaje final que dice **"Building EXE from ... completed successfully."**

El archivo final se encuentra en:

```text
EchoSeal/
├── build/          <-- Archivos temporales (puedes borrarlos)
├── dist/           <-- 📂 AQUÍ ESTÁ TU EJECUTABLE
│   └── EchoSeal.exe
├── main.spec       <-- Archivo de configuración de la build
└── ...
```

Puedes copiar `EchoSeal.exe` de la carpeta `dist` y llevarlo en un USB a cualquier otro equipo. **No requiere instalación** en el equipo de destino.

---

## 🧹 6. Limpieza

Después de compilar y extraer tu archivo `.exe`, puedes limpiar tu directorio de trabajo ejecutando:

**Windows:**
```bash
rmdir /s /q build
rmdir /s /q dist
del EchoSeal.spec
```

**Linux/Mac:**
```bash
rm -rf build dist EchoSeal.spec
```
```
