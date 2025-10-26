# Con esto definimos en nuestro entorno la conexión a IBM Quantum Platform de manera correcta.
from src.utils.ibm_auth import save_account_to_disk

try:
    save_account_to_disk()
except RuntimeError as e:
    print(e) 