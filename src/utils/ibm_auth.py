# src/utils/ibm_auth.py
import os
from dotenv import load_dotenv
from qiskit_ibm_runtime import QiskitRuntimeService

load_dotenv()  # carga .env en desarrollo local

IBM_TOKEN = os.getenv("IBM_TOKEN")
IBM_INSTANCE = os.getenv("IBM_INSTANCE") 
IBM_CHANNEL = os.getenv("IBM_CHANNEL", "ibm_quantum_platform")  # para cuántica utilizar: "ibm_quantum_platform"

def save_account_to_disk(token: str = None, instance: str | None = None): 
    token = token or IBM_TOKEN
    instance = instance or IBM_INSTANCE
    if not token:
        raise RuntimeError("No IBM token found in environment.")
    # guarda en el entorno virtual
    QiskitRuntimeService.save_account(
        token=token,
        instance=instance,
        channel=IBM_CHANNEL,
        set_as_default=True,
        overwrite=True,
    )
    print("Cuenta guardada en el entorno virtual.")

def get_service():
    # carga la cuenta por defecto guardad con save_account().
    return QiskitRuntimeService()
