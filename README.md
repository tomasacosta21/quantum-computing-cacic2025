# Introducción a la Computación Cuántica - CACIC 2025

Este repositorio contiene el contenido práctico y teórico visto durante el curso de Introducción a la Computación Cuántica y Aplicaciones Prácticas del CACIC 2025, dictado por el Dr. Andrés Alejandro Reynoso, docente de la Universidad Nacional de Río Negro - Sede Andina. Este curso fue dictado bajo el marco de la XXIX Escuela Internacional de Informática y el XXXI Congreso Argentino de Ciencias de la Computación (CACIC) 2025.
## Contenido

El repositorio incluye varios cuadernos Jupyter (notebooks) que cubren distintos temas:

1.  **Conceptos Fundamentales (TP N° 1) (`docs/qubits_fundamentals.ipynb`)**:
    * Exploración de bases alternativas (X, Y, Z).
    * Notación de Dirac y productos internos.
    * Matrices de Pauli y sus propiedades.
    * Representación de estados de espín en direcciones arbitrarias.

2.  **Protocolos de Comunicación Cuántica (TP N° 2) (`notebooks/sdc-&-teleportation/`)**:
    * **Codificación Superdensa (`sdc.ipynb`)**: Demuestra el envío de dos bits clásicos utilizando un único qubit entrelazado.
    * **Teleportación Cuántica (`teleportation.ipynb`)**: Implementa el protocolo para transferir un estado cuántico utilizando comunicación clásica y entrelazamiento.

3.  **Algoritmos Cuánticos con Oráculos (TP N° 3) (`notebooks/oracle-algorithms/`)**:
    * **Algoritmo de Deutsch (`deutchs-algorithm.ipynb`)**: Resuelve el problema de Deutsch (función constante vs. balanceada) con una sola consulta.
    * **Algoritmo de Deutsch-Jozsa (`deutch-jozsa-algorithm.ipynb`)**: Generaliza el algoritmo de Deutsch para funciones de n-bits.
    * **Algoritmo de Simon (`simons-algorithm.ipynb`)**: Demuestra cómo encontrar un período oculto (máscara XOR) exponencialmente más rápido que los métodos clásicos.

---
## Estructura del Proyecto

* **`docs/`**: Contiene notebooks relacionados con la teoría fundamental.
* **`notebooks/`**: Contiene implementaciones prácticas de protocolos y algoritmos cuánticos.
* **`src/`**: Contiene módulos de utilidad en Python, como asistentes para la autenticación con IBM Quantum.
* **`requirements.txt`**: Lista los paquetes de Python necesarios.
* **`setup.py`**: Configuración para instalar el directorio `src` como un paquete local.
* **`.env` / `secrets.env`**: (No incluido, debe crearse localmente) Se utiliza para almacenar las credenciales de la API de IBM Quantum.
* **`.gitignore`**: Especifica los archivos y directorios ignorados por Git.

---
## Configuración y Ejecución

1.  **Clonar el Repositorio:**
    ```bash
    git clone <url-del-repositorio>
    cd quantum-computing-cacic2025
    ```

2.  **Crear y Activar Entorno Virtual:**
    ```bash
    python -m venv .venv
    # En Windows (PowerShell)
    .\.venv\Scripts\Activate.ps1
    # En macOS/Linux
    source .venv/bin/activate
    ```

3.  **Instalar Dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Instalar Pa
