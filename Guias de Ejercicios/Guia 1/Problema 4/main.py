import math

def bisecciones_necesarias(a, b, delta):
    """
    Calcula el numero minimo de bisecciones necesarias
    para que el error sea menor que delta
    """
    # De |r - c| <= |b - a| / 2^n <= delta
    # Despejamos: n >= log2(|b - a| / delta)
    
    intervalo = abs(b - a)
    n_exacto = math.log2(intervalo / delta)
    n_minimo = math.ceil(n_exacto)
    
    return n_minimo

# Ejemplo de uso
if __name__ == "__main__":
    # Caso ejemplo: intervalo [0, 1] con error < 0.01
    a, b = 0, 1
    delta = 0.01
    
    n = bisecciones_necesarias(a, b, delta)
    
    print(f"Intervalo: [{a}, {b}]")
    print(f"Error deseado: {delta}")
    print(f"Bisecciones necesarias: {n}")
    
    # Verificacion
    error_real = abs(b - a) / (2**n)
    print(f"Error real con {n} bisecciones: {error_real:.6f}")
    print(f"Cumple condicion: {error_real <= delta}")