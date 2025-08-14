from funciones import f, calcular_error

def metodo_secante(x0, x1, tolerancia=1e-3, tipo_error='absoluto', max_iter=100, mostrar_iteraciones=True):
    """
    Método de la Secante para encontrar raíces
    
    Args:
        x0: Primer valor inicial
        x1: Segundo valor inicial  
        tolerancia: Tolerancia para el error
        tipo_error: 'absoluto' o 'porcentual'
        max_iter: Numero máximo de iteraciones
        mostrar_iteraciones: Si mostrar el proceso iterativo
    
    Returns:
        La raiz encontrada o None si no converge
    """
    print(f"\n=== METODO DE LA SECANTE ===")
    print(f"Valores iniciales: x0 = {x0}, x1 = {x1}")
    print(f"Tolerancia: {tolerancia}")
    print(f"Tipo de error: {tipo_error}")
    
    unidad_error = "%" if tipo_error == 'porcentual' else ""
    
    if mostrar_iteraciones:
        print(f"\n{'Iter':<4} {'x0':<12} {'x1':<12} {'f(x0)':<12} {'f(x1)':<12} {'Error':<12}")
        print("-" * 80)
    
    i = 0
    error = float('inf')
    
    while error > tolerancia and i < max_iter:
        fx0 = f(x0)
        fx1 = f(x1)
        
        # Verificar que f(x1) - f(x0) no sea cero
        if abs(fx1 - fx0) < 1e-10:
            print("ERROR: Denominador muy chico, el metodo no converge")
            return None
        
        # Calcular nueva aproximacion usando la formula de la secante
        x2 = x0 - fx0 * (x1 - x0) / (fx1 - fx0)
        error = calcular_error(x2, x1, tipo_error)
        
        if mostrar_iteraciones:
            print(f"{i+1:<4} {x0:<12.6f} {x1:<12.6f} {fx0:<12.6f} {fx1:<12.6f} {error:<12.6f}{unidad_error}")
        
        # Actualizar valores para la siguiente iteracion
        x0 = x1
        x1 = x2
        i += 1
    
    print(f"\n=== RESULTADOS ===")
    print(f"Raiz encontrada: x = {x1:.8f}")
    print(f"f({x1:.8f}) = {f(x1):.8f}")
    print(f"Error final: {error:.8f}{unidad_error}")
    print(f"NNumero de iteraciones: {i}")
    print(f"Tolerancia requerida: {tolerancia}{unidad_error}")
    
    if error <= tolerancia:
        return x1
    else:
        print("ERROR: No se alcanzo la tolerancia en el numero maximo de iteraciones")
        return None
