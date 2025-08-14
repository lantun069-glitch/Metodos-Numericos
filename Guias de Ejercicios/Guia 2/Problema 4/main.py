from newton_raphson import newton_raphson
from funciones import f

def main():
    print("DATOS")
    print("Hoja metalica: 10 x 16 cm")
    print("Volumen requerido: 100 cm³")
    print("Ecuacion: (10-2x)(16-2x)x = 100")
    print()
    
    # Resolver con Newton-Raphson
    # Valor inicial x0 = 1.5 (estimacion razonable)
    x0 = 1.5
    tolerancia = 1e-9
    
    solucion = newton_raphson(x0, tolerancia, 'absoluto')
    
    if solucion is not None:
        print(f"\nSOLUCION:")
        print(f"Lado del cuadrado a recortar: x = {solucion:.9f} cm")
        
        # Verificar resultado
        largo = 16 - 2*solucion
        ancho = 10 - 2*solucion
        altura = solucion
        volumen = largo * ancho * altura
        
        print(f"Dimensiones del contenedor:")
        print(f"Largo: {largo:.6f} cm")
        print(f"Ancho: {ancho:.6f} cm")
        print(f"Altura: {altura:.6f} cm")
        print(f"Volumen: {volumen:.6f} cm³")
        print(f"Verificacion f(x) = {f(solucion):.2e}")

if __name__ == "__main__":
    main()