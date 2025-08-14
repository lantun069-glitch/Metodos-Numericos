from biseccion import biseccion
from funciones import f
import math

# Buscar intervalo donde f cambia de signo
# Probamos algunos valores para encontrar el intervalo
a = 1.5  # T2/T1 = 1.5
b = 3.0  # T2/T1 = 3.0

print(f"f({a}) = {f(a):.6f}")
print(f"f({b}) = {f(b):.6f}")
print()

# Resolver con biseccion
resultado = biseccion(a, b)

print(f"\nResultado: T2/T1 = {resultado:.6f}")

# Verificacion
gamma = 1/resultado
ln_ratio = math.log(resultado)
eta = (ln_ratio - (1 - gamma)) / (ln_ratio + gamma)
print(f"Eficiencia obtenida: {eta:.4f} = {eta*100:.1f}%")