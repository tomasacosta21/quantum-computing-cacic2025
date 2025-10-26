"""API pública del paquete quantum-computing-cacic2025."""

__version__ = "0.1.0"
__author__ = "Tomás Acosta Oyarzabal - tomsacosta19@gmail.com - github.com/tomasacosta21"

from .utils.ibm_auth import get_service  

__all__ = ["get_service", "__version__"]