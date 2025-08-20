from sistema_polinomio import eliminacion_gaussiana, calcular_determinante, calcular_norma_frobenius

def main():
    # Sistema original con A11 = 20514
    A1 = [
        [20514.0, 4424.0, 978.0, 224.0],
        [4424.0, 978.0, 224.0, 54.0],
        [978.0, 224.0, 54.0, 14.0],
        [224.0, 54.0, 14.0, 4.0]
    ]
    b = [20514.0, 4424.0, 978.0, 224.0]
    
    print("1. Sistema original (A11 = 20514):")
    c1 = eliminacion_gaussiana(A1, b)
    print(f"   c1 = {c1[0]:.1f}, c2 = {c1[1]:.1f}, c3 = {c1[2]:.1f}, c4 = {c1[3]:.1f}")
    det1 = calcular_determinante(A1)
    norma1 = calcular_norma_frobenius(A1)
    print(f"   det(A) = {det1:.0f}, ||A|| = {norma1:.0f}")
    
    # Sistema modificado con A11 = 20515
    A2 = [
        [20515.0, 4424.0, 978.0, 224.0],
        [4424.0, 978.0, 224.0, 54.0],
        [978.0, 224.0, 54.0, 14.0],
        [224.0, 54.0, 14.0, 4.0]
    ]
    
    print("\n2. Sistema perturbado (A11 = 20515):")
    c2 = eliminacion_gaussiana(A2, b)
    print(f"   c1 = {c2[0]:.6f}, c2 = {c2[1]:.3f}, c3 = {c2[2]:.6f}, c4 = {c2[3]:.5f}")
    det2 = calcular_determinante(A2)
    norma2 = calcular_norma_frobenius(A2)
    print(f"   det(A) = {det2:.0f}, ||A|| = {norma2:.0f}")
    
    # Verificacion del mal condicionamiento
    print("\nVerificacion: La matriz esta mal condicionada")
    print(f"Cambio en A11: {(20515-20514)/20514*100:.004f}%")
    print(f"Cambio en det: {abs(det2-det1)/abs(det1)*100:.1f}%")
    print(f"Razon |det|/||A||: {abs(det1)/norma1:.6f} (muy pequena)")

if __name__ == "__main__":
    main()