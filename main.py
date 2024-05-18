import subprocess
import sys
from run import *


def install_requirements():
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
        )
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)


def main():
    # Aquí va tu código principal
    print("Dependencias instaladas. Ejecutando el programa principal...")
    # Ejemplo: import tu_modulo_principal
    Run()


if __name__ == "__main__":
    install_requirements()
    main()
