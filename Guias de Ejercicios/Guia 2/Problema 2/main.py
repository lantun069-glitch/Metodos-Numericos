from punto_fijo import punto_fijo
from funciones import g1, g2, g3
from graficos import graficar_funcion

def main():
    print("PUNTOS FIJOS DE FUNCIONES")
    print("=" * 40)
    
    # Funcion 1: g(x) = x^5 - 3x^3 - 2x^2 + 2
    print("1. g(x) = x^5 - 3x^3 - 2x^2 + 2")
    punto1 = punto_fijo(g1, 1.0)
    if punto1:
        print(f"   Punto fijo: {punto1:.12f}")
    else:
        print("   No converge")
    graficar_funcion(g1, "x^5 - 3x^3 - 2x^2 + 2", -2, 2, punto1)
    
    # Funcion 2: g(x) = cos(sin(x))
    print("2. g(x) = cos(sin(x))")
    punto2 = punto_fijo(g2, 0.5)
    if punto2:
        print(f"   Punto fijo: {punto2:.12f}")
    else:
        print("   No converge")
    graficar_funcion(g2, "cos(sin(x))", -2, 2, punto2)
    
    # Funcion 3: g(x) = x^(x-cos(x))
    print("3. g(x) = x^(x-cos(x))")
    punto3 = punto_fijo(g3, 1.2)
    if punto3:
        print(f"   Punto fijo: {punto3:.12f}")
    else:
        print("   No converge")
    graficar_funcion(g3, "x^(x-cos(x))", 0.5, 2, punto3)

if __name__ == "__main__":
    main()