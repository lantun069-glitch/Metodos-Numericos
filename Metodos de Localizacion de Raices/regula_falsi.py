from funciones import f, calcular_error

def regula_falsi(a, b, tolerancia=1e-5, tipo_error='absoluto', max_iter=100):
    if f(a) * f(b) >= 0:
        print("No se garantiza la existencia de una raíz en el intervalo [a, b].")
        return None

    iteracion = 0
    c_viejo = None
    
    print(f"Iteracion\ta\t\tb\t\tc\t\tf(c)\t\tError ({tipo_error})")
    print("-" * 80)

    while iteracion < max_iter:
        c = a - f(a) * (b - a) / (f(b) - f(a))
        
        # Calcular error despues de la primera iteracion
        if c_viejo is not None:
            error = calcular_error(c, c_viejo, tipo_error)
            error_str = f"{error:.6f}"
        else:
            error_str = "---"
        
        print(f"{iteracion + 1}\t\t{a:.6f}\t{b:.6f}\t{c:.6f}\t{f(c):.6f}\t{error_str}")

        # Verificar si encontramos la raíz exacta
        if abs(f(c)) < 1e-10:
            print(f"\n[Regla Falsi] Raiz exacta encontrada: {c:.6f}")
            return c
        
        # Verificar criterio de parada despues de la primera iteracin
        if c_viejo is not None and error <= tolerancia:
            print(f"\n[Regla Falsi] Convergencia alcanzada:")
            print(f"Raiz aproximada: {c:.6f}")
            print(f"f({c:.6f}) = {f(c):.6f}")
            print(f"Error final: {error:.6f}")
            return c

        # Actualizar intervalo
        if f(a) * f(c) > 0:
            a = c
        elif f(a) * f(c) < 0:
            b = c
        else:
            break

        c_viejo = c
        iteracion += 1

    # Si se alcanzo el maximo de iteraciones
    if c_viejo is not None:
        error = calcular_error(c, c_viejo, tipo_error)
    print(f"\n[Regla Falsi] Maximo de iteraciones alcanzado:")
    print(f"Raiz aproximada: {c:.6f}")
    print(f"f({c:.6f}) = {f(c):.6f}")
    if c_viejo is not None:
        print(f"Error final: {error:.6f}")
    return c
