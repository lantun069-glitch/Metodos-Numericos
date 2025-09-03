def interpolacion_lagrange(puntos_x, puntos_y, x_interpolar):
    """Metodo de Lagrange para interpolacion polinomial"""
    n = len(puntos_x)
    suma = 0.0
    
    for i in range(n):
        # Calcular Li(x)
        producto = 1.0
        for k in range(n):
            if k != i:
                producto *= (x_interpolar - puntos_x[k]) / (puntos_x[i] - puntos_x[k])
        
        # Sumar Li(x) * yi
        suma += puntos_y[i] * producto
    
    return suma

def main():
    # Datos del problema
    temperatura = [-200.15, -200, -100, 0, 100, 300]  # grados Celsius
    cp = [0.1, 0.45, 0.699, 0.87, 0.941, 1.04]  # kJ/(kg·K)
    
    print("PROBLEMA 3: Calor especifico del aluminio")
    print("="*50)
    print("\nDatos experimentales:")
    print("T [C]    cp [kJ/(kg·K)]")
    for i in range(len(temperatura)):
        print(f"{temperatura[i]:7.2f}    {cp[i]:.3f}")
    
    # Interpolar para T = 500 C
    T_interpolar = 500
    cp_500 = interpolacion_lagrange(temperatura, cp, T_interpolar)
    
    print(f"\n{'='*50}")
    print(f"Resultado para T = {T_interpolar} C:")
    print(f"cp interpolado = {cp_500:.4f} kJ/(kg·K)")
    
    # Verificar con puntos conocidos
    print(f"\n{'='*50}")
    print("Verificacion (el polinomio debe pasar por los puntos):")
    for i in range(len(temperatura)):
        cp_calc = interpolacion_lagrange(temperatura, cp, temperatura[i])
        print(f"T = {temperatura[i]:7.2f}: cp = {cp_calc:.4f} (real: {cp[i]:.3f})")
    
    # Analisis del resultado
    print(f"\n{'='*50}")
    print("ANALISIS:")
    print(f"El valor obtenido cp({T_interpolar}) = {cp_500:.4f} kJ/(kg·K)")
    
    if cp_500 < 0:
        print("PROBLEMA: Valor negativo (fisicamente imposible)")
        print("Causa: Extrapolacion muy lejana con polinomio de grado alto")
    elif cp_500 > 1.5:
        print("ADVERTENCIA: Valor muy alto para aluminio")
        print("El polinomio oscila fuera del rango de datos")
    
    print("\nConclusion:")
    print("- Lagrange es adecuado para INTERPOLACION (dentro del rango)")
    print("- Para EXTRAPOLACION a 500 C (muy lejos del rango) no es apropiado")
    print("- Un valor fisicamente razonable seria ~1.1 kJ/(kg·K)")
    print("  (considerando que cp tiende a estabilizarse)")

if __name__ == "__main__":
    main()