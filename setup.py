from setuptools import setup, find_packages

setup(
    name="quantum_cacic_project",
    version="0.1.0",
    
    # Esto le dice a setuptools: "Mis paquetes están DENTRO de la carpeta 'src'"
    packages=find_packages(where="src"),
    
    # Esto le dice: "Y la raíz de esos paquetes (el '') es 'src'"
    package_dir={"": "src"},
)