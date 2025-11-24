from setuptools import setup, find_packages
import platform

# Definir dependencias base
requirements = [
    "psutil",
    "colorama",
    "pyinstaller"
]

# Dependencias solo para Windows
if platform.system() == "Windows":
    requirements.append("wmi")

setup(
    name="EchoSeal",
    version="1.0.0",
    description="Sistema de Detección de Manipulación de Entornos Virtuales y Sandboxing Oculto",
    author="Tu Nombre",
    author_email="tu_email@ejemplo.com",
    url="https://github.com/TU_USUARIO/EchoSeal",
    packages=find_packages(),  # Busca automáticamente las carpetas modules/ y utils/
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            # Esto permite ejecutar 'echoseal' desde la terminal directamente
            'echoseal=main:main', 
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Topic :: Security",
    ],
    python_requires='>=3.8',
)
