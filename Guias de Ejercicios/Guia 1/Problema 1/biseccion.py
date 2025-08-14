from funciones import f, calcular_error

def biseccion(a, b, tolerancia=1e-5, tipo_error='absoluto', max_iter=100):
    if f(a) * f(b) >= 0:
        print("No se garantiza la existencia de una raiz en el intervalo [a, b].")
        return None, None
    
    iteracion = 0
    c_viejo = None
    error_final = None
    
    print(f"Iter\t{'a':<10}\t{'b':<10}\t{'c':<10}\t{'f(c)':<12}\t{'Error':<10}")
    print("-" * 70)
    
    while iteracion < max_iter:
        c = (a + b) / 2
        
        if c_viejo is not None:
            error = calcular_error(c, c_viejo, tipo_error)
            error_str = f"{error:.6f}"
            error_final = error
        else:
            error_str = "---"
        
        print(f"{iteracion + 1}\t{a:<10.6f}\t{b:<10.6f}\t{c:<10.6f}\t{f(c):<12.6f}\t{error_str}")
        
        if abs(f(c)) < 1e-10:
            return c, error_final
        
        if c_viejo is not None and error <= tolerancia:
            return c, error_final
        
        if f(a) * f(c) > 0:
            a = c
        elif f(a) * f(c) < 0:
            b = c
        else:
            break
        
        c_viejo = c
        iteracion += 1
    
    return c, error_final