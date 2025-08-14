from funciones import f, calcular_error

def biseccion_con_historial(a, b, tolerancia=1e-5, tipo_error='absoluto', max_iter=100):
    """
    Metodo de biseccion que retorna historial de errores e iteraciones
    """
    if f(a) * f(b) >= 0:
        print("No se garantiza la existencia de una raiz en el intervalo [a, b].")
        return None, [], []
    
    iteracion = 0
    c_viejo = None
    errores = []
    iteraciones = []
    
    print(f"=== METODO DE BISECCION ===")
    print(f"Intervalo inicial: [{a}, {b}]")
    print(f"Tolerancia: {tolerancia}")
    print(f"Tipo de error: {tipo_error}")
    print(f"\nIteracion\ta\t\tb\t\tc\t\tf(c)\t\tError ({tipo_error})")
    print("-" * 90)
    
    while iteracion < max_iter:
        c = (a + b) / 2
        
        if c_viejo is not None:
            error = calcular_error(c, c_viejo, tipo_error)
            error_str = f"{error:.8f}"
            errores.append(error)
            iteraciones.append(iteracion + 1)
        else:
            error_str = "---"
        
        print(f"{iteracion + 1}\t\t{a:.6f}\t{b:.6f}\t{c:.6f}\t{f(c):.6f}\t{error_str}")
        
        if abs(f(c)) < 1e-12:
            print(f"\nRaiz exacta encontrada: {c:.8f}")
            break
            
        if c_viejo is not None and error <= tolerancia:
            print(f"\nConvergencia alcanzada en {iteracion + 1} iteraciones")
            print(f"Raiz aproximada: {c:.8f}")
            print(f"f({c:.8f}) = {f(c):.8f}")
            print(f"Error final: {error:.8f}")
            break
        
        if f(a) * f(c) > 0:
            a = c
        elif f(a) * f(c) < 0:
            b = c
        else:
            break
            
        c_viejo = c
        iteracion += 1
    
    return c, errores, iteraciones