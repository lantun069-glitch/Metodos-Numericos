import math
from newton_raphson import newton_raphson

# Punto 1: Verificacion
print("1. Verificacion catenaria y = 9.1889*cosh(x/9.1889) - 9.1889 en (±10; 6)")
C = 9.1889
x = 10  # Para x = ±10 (por simetria del cosh)
y_calc = C * math.cosh(x/C) - C
print(f"   y calculado = {y_calc:.4f}")
print(f"   Error = {abs(y_calc - 6):.6f}")

# Punto 2: Encontrar C para puntos (±12; 5)
print("\n2. Catenaria para puntos (±12; 5)")
print("   Resolviendo: C*cosh(12/C) - C = 5")

C_inicial = 8.0
C_solucion = newton_raphson(C_inicial)

if C_solucion:
    print(f"   C = {C_solucion:.6f}")
    print(f"   Catenaria: y = {C_solucion:.6f}*cosh(x/{C_solucion:.6f}) - {C_solucion:.6f}")
    
    # Verificacion
    y_verif = C_solucion * math.cosh(12/C_solucion) - C_solucion
    print(f"   Verificacion en x=±12: y = {y_verif:.6f}")