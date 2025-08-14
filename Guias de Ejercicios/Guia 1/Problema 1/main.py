from biseccion import biseccion
from graficar import graficar_funcion
from funciones import f

def main():
    print("PROBLEMA 1")
    print("=" * 50)
    
    # Graficar funcion
    graficar_funcion()
    print("Grafico guardado como 'grafico_funcion.png'\n")
    
    # Verificar intervalo [0, 1]
    a, b = 0, 1
    print(f"Verificando intervalo [{a}, {b}]:")
    print(f"f({a}) = {f(a):.6f}")
    print(f"f({b}) = {f(b):.6f}")
    
    if f(a) * f(b) < 0:
        tolerancia = 1e-4
        raiz, error_final = biseccion(a, b, tolerancia=tolerancia, tipo_error='absoluto')
        
        print(f"\nRaiz encontrada: x = {raiz:.6f}")
        print(f"f({raiz:.6f}) = {f(raiz):.8f}")
        if error_final is not None:
            print(f"Error final: {error_final:.8f}")
    else:
        print("No hay cambio de signo en [0, 1]")

if __name__ == "__main__":
    main()

"""
RESPUESTAS A PREGUNTAS DEL ENUNCIADO:

-El grafico nos permite ver las raíces de la funcion de grado 3
-El metodo de biseccion encuentra la raiz mas chica en [0,1] con tolerancia 1e-4
"""