# interpolacion_lagrange.py
from typing import List, Tuple

def leer_datos(nombre_archivo: str) -> Tuple[List[float], List[float]]:
    """
    Lee los datos de interpolacion desde un archivo de texto.
    El archivo debe tener el formato:
    x0 y0
    x1 y1
    x2 y2
    ...
    """
    puntos_x = []
    puntos_y = []
    
    # Si no tiene extension, agregar .txt automaticamente
    if '.' not in nombre_archivo:
        nombre_archivo += '.txt'
    
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                # Ignorar lineas vacias y comentarios
                linea = linea.strip()
                if linea and not linea.startswith('#'):
                    # Separar los valores x e y
                    valores = linea.split()
                    if len(valores) >= 2:
                        x = float(valores[0])
                        y = float(valores[1])
                        puntos_x.append(x)
                        puntos_y.append(y)
    except FileNotFoundError:
        print(f"Error: No se encontro el archivo '{nombre_archivo}'")
        print("Asegurate de que el archivo existe en el directorio actual")
        print("Formato esperado: cada linea debe contener 'x y' separados por espacio")
        return [], []
    except ValueError as e:
        print(f"Error al leer los datos: {e}")
        return [], []
    
    return puntos_x, puntos_y

def interpolacion_lagrange(puntos_x: List[float], puntos_y: List[float], x_interpolar: float) -> float:
    """
    Realiza interpolacion polinomial usando el metodo de Lagrange.
    Implementacion del pseudocodigo de la clase.
    
    Parametros:
    -----------
    puntos_x : Lista de coordenadas x de los puntos conocidos
    puntos_y : Lista de coordenadas y de los puntos conocidos  
    x_interpolar : Valor de x donde se desea interpolar
    
    Retorna:
    --------
    Valor interpolado de y en x_interpolar
    """
    
    n = len(puntos_x)
    
    # Verificar que los arrays tengan la misma longitud
    if len(puntos_y) != n:
        raise ValueError("Los arrays x e y deben tener la misma longitud")
    
    # Inicializar suma
    suma = 0.0
    
    # Para cada punto i
    for i in range(n):
        # Inicializar producto para Li(x)
        producto = 1.0
        
        # Calcular el coeficiente de Lagrange Li(x)
        for k in range(n):
            if k != i:
                # Multiplicar por (x - xk) / (xi - xk)
                producto = producto * (x_interpolar - puntos_x[k]) / (puntos_x[i] - puntos_x[k])
        
        # Sumar el termino Li(x) * yi a la suma total
        suma = suma + puntos_y[i] * producto
    
    return suma

def main():
    """
    Programa principal para interpolacion de Lagrange
    """
    
    print("="*50)
    print("INTERPOLACION POLINOMIAL - METODO DE LAGRANGE")
    print("="*50)
    
    # Leer nombre del archivo
    print("\nFormato del archivo: cada linea debe contener 'x y' separados por espacio")
    print("Ejemplo: datos.txt (la extension .txt se agrega automaticamente si no se especifica)")
    nombre_archivo = input("\nIngrese el nombre del archivo de datos: ")
    
    # Leer los datos del archivo
    puntos_x, puntos_y = leer_datos(nombre_archivo)
    
    if not puntos_x:
        print("No se pudieron leer los datos del archivo")
        return
    
    # Mostrar los puntos leidos
    print(f"\nSe leyeron {len(puntos_x)} puntos del archivo:")
    print("-"*30)
    for i in range(len(puntos_x)):
        print(f"Punto {i}: x{i} = {puntos_x[i]:.4f}, y{i} = {puntos_y[i]:.4f}")
    
    # Solicitar el punto a interpolar
    print("\n" + "-"*30)
    x_interpolar = float(input("Ingrese el valor de x donde desea interpolar: "))
    
    # Realizar la interpolacion
    resultado = interpolacion_lagrange(puntos_x, puntos_y, x_interpolar)
    
    # Mostrar el resultado
    print("\n" + "="*50)
    print("RESULTADO:")
    print(f"P({x_interpolar}) = {resultado:.6f}")
    print("="*50)

# Ejecutar el programa
if __name__ == "__main__":
    main()