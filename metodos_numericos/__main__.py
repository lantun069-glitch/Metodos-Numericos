"""
Punto de entrada para ejecutar el paquete metodos_numericos como modulo.
"""

if __name__ == "__main__":
    import sys
    import os
    
    # Agregar el directorio padre al path
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, parent_dir)
    
    # Cambiar al directorio padre para imports relativos
    os.chdir(parent_dir)
    
    # Ejecutar el main.py
    with open('main.py', 'r') as f:
        exec(f.read())