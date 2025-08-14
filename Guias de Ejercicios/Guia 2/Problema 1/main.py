from punto_fijo import punto_fijo
from funciones import dg_dx

# Resolver g(x) = x^2 + x - 4 por punto fijo
print("Resolviendo g(x) = x^2 + x - 4")

# Los puntos fijos teoricos son x = 2 y x = -2
puntos_fijos = [2, -2]

for p in puntos_fijos:
    derivada = dg_dx(p)
    print(f"\nPunto fijo teorico: x = {p}")
    print(f"g'({p}) = {derivada}")
    print(f"|g'({p})| = {abs(derivada)} {'< 1' if abs(derivada) < 1 else '>= 1'}")

# Probar iteracion desde x0 = 1
print(f"\n--- Iteracion desde x0 = 1 ---")
resultado = punto_fijo(1.0, tolerancia=1e-6)

if resultado:
    print(f"Convergio a: {resultado:.6f}")
else:
    print("No convergio")

"""
RESPUESTAS A PREGUNTAS DEL ENUNCIADO:

¿Podemos utilizar iteración de punto fijo?
Técnicamente sí, pero no convergerá porque |g'(P)| > 1 en ambos puntos fijos.

Ventaja de tener g'(P) ≈ 0:
Si |g'(P)| < 1: el método converge
Si g'(P) ≈ 0: convergencia muy rápida
En nuestro caso: g'(2) = 5 y g'(-2) = -3, ambos con |g'(P)| > 1, por lo que diverge
"""