from newton_raphson import newton_raphson
from funciones import f
import math

def main():
    print("SOLUCION: Profundidad de sumersion de esfera")
    print("Datos: r=10cm, densidad=0.638 gr/cm³")
    print("-" * 45)
    
    # Estimacion inicial 
    x0 = 10.0  
    tolerancia = 1e-4
    
    resultado = newton_raphson(x0, tolerancia)
    
    if resultado:
        # Verificacion
        V_esfera = (4/3) * math.pi * 10**3
        V_sumergido = math.pi * resultado**2 * (30 - resultado) / 3
        porcentaje = (V_sumergido / V_esfera) * 100
        
        print(f"\nResultado: d = {resultado:.4f} cm")
        print(f"Verificacion: f({resultado:.4f}) = {f(resultado):.8f}")
        print(f"Volumen sumergido: {porcentaje:.1f}%")

if __name__ == "__main__":
    main()