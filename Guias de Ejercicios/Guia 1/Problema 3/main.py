from biseccion import biseccion
from regula_falsi import regula_falsi
from funciones import f

def main():
    # Buscar intervalo donde f cambie de signo
    a, b = None, None
    for m in range(10, 200, 10):
        if f(m) < 0:
            a = m
        elif f(m) > 0 and a is not None:
            b = m
            break
    
    if a is None or b is None:
        print("No se encontro intervalo valido")
        return
    
    tolerancia = 1e-3
    
    # Resolver con biseccion
    masa_biseccion = biseccion(a, b, tolerancia)
    
    # Resolver con regla falsi
    masa_regla_falsi = regula_falsi(a, b, tolerancia)
    
    print("RESULTADOS:")
    if masa_biseccion:
        print(f"Biseccion: m = {masa_biseccion:.3f} kg")
    if masa_regla_falsi:
        print(f"Regla Falsi: m = {masa_regla_falsi:.3f} kg")

if __name__ == "__main__":
    main()