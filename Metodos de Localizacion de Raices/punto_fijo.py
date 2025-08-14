from funciones import g, calcular_error

def punto_fijo(x0, tolerancia=1e-3, tipo_error='absoluto', max_iter=100, mostrar_iteraciones=True):
    """
    Método de Punto Fijo para encontrar raíces
    
    Args:
        x0: Valor inicial
        tolerancia: Tolerancia para el error
        tipo_error: 'absoluto' o 'porcentual'
        max_iter: Número máximo de iteraciones
        mostrar_iteraciones: Si mostrar el proceso iterativo
    
    Returns:
        El punto fijo encontrado o None si no converge
    """
    print(f"\n=== MÉTODO DE PUNTO FIJO ===")
    print(f"Valor inicial: x0 = {x0}")
    print(f"Tolerancia: {tolerancia}")
    print(f"Tipo de error: {tipo_error}")
    
    unidad_error = "%" if tipo_error == 'porcentual' else ""
    
    if mostrar_iteraciones:
        print(f"\n{'Iter':<4} {'x':<12} {'g(x)':<12} {'Error':<12}")
        print("-" * 50)
    
    i = 0
    x = x0
    error = float('inf')
    
    while error > tolerancia and i < max_iter:
        x_nuevo = g(x)
        error = calcular_error(x_nuevo, x, tipo_error)
        
        if mostrar_iteraciones:
            print(f"{i+1:<4} {x:<12.6f} {x_nuevo:<12.6f} {error:<12.6f}{unidad_error}")
        
        x = x_nuevo
        i += 1
    
    print(f"\n=== RESULTADOS ===")
    print(f"Punto fijo encontrado: x = {x:.8f}")
    print(f"g({x:.8f}) = {g(x):.8f}")
    print(f"Error final: {error:.8f}{unidad_error}")
    print(f"Numero de iteraciones: {i}")
    print(f"Tolerancia requerida: {tolerancia}{unidad_error}")
    
    if error <= tolerancia:
        return x
    else:
        print("ERROR: No se alcanzo la tolerancia en el numero maximo de iteraciones")
        return None
