from eliminacion_gaussiana import resolver_sistema, verificar_solucion

def main():
    # Sistema del Problema 4
    A = [
        [ 4.0, -2.0,  1.0],
        [-2.0,  1.0, -1.0],
        [-2.0,  3.0,  6.0]
    ]
    
    b = [2.0, -1.0, 0.0]
    
    print("=" * 60)
    print("PROBLEMA 4: ELIMINACION GAUSSIANA CON PIVOTEO PARCIAL")
    print("=" * 60)
    
    # Resolver el sistema
    solucion = resolver_sistema(A, b)
    
    # Mostrar solucion
    print("\n=== SOLUCION DEL SISTEMA ===")
    print(f"x1 = {solucion[0]:.6f}")
    print(f"x2 = {solucion[1]:.6f}")
    print(f"x3 = {solucion[2]:.6f}")
    
    # Verificar solucion
    error_max = verificar_solucion(A, b, solucion)
    print(f"\nError maximo en la verificacion: {error_max:.2e}")
    
    if error_max < 1e-10:
        print("La solucion es correcta")
    else:
        print("Advertencia: La solucion puede no ser precisa")

if __name__ == "__main__":
    main()