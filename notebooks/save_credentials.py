# Con esto definimos en nuestro entorno la conexión a IBM Quantum Platform de manera correcta.
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:\Users\Sebas Acosta\Desktop\quantum-computing-cacic2025\src\utils\ibm_auth.py'))
sys.path.insert(0, project_root)

from src.utils.ibm_auth import save_account_to_disk



try:
    save_account_to_disk()
except RuntimeError as e:
    print(e) 