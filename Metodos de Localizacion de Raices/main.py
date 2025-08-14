from biseccion import biseccion
from regula_falsi import regula_falsi
from newton_raphson import newton_raphson
from metodo_de_la_secante import metodo_secante
from punto_fijo import punto_fijo
from funciones import solicitar_tipo_error, solicitar_tolerancia

def main():
    print("=" * 70)
    print("           METODOS DE LOCALIZACION DE RAICES")
    print("=" * 70)
    print("1. Biseccion")
    print("2. Regla Falsi (Falsa Posicion)")
    print("3. Newton-Raphson")
    print("4. Metodo de la Secante")
    print("5. Punto Fijo")
    print("0. Salir")
    print("=" * 70)
    
    try:
        opcion = input("\nSelecciona el metodo (0-5): ")
        
        if opcion == "0":
            print("Saliendo del programa")
            return
            
        elif opcion in ["1", "2"]:
            # Metodos que requieren intervalo [a, b]
            print(f"\n--- {'BISECCION' if opcion == '1' else 'REGLA FALSI'} ---")
            print("Nota: Necesitas un intervalo [a, b] donde f(a) y f(b) tengan signos opuestos")
            
            a = float(input("Ingresa el valor de a: "))
            b = float(input("Ingresa el valor de b: "))
            tipo_error = solicitar_tipo_error()
            tolerancia = solicitar_tolerancia(tipo_error)
            
            if opcion == "1":
                biseccion(a, b, tolerancia, tipo_error)
            else:
                regula_falsi(a, b, tolerancia, tipo_error)
                
        elif opcion in ["3", "4", "5"]:
            # Metodos que requieren valor(es) inicial(es)
            nombres = {"3": "NEWTON-RAPHSON", "4": "METODO DE LA SECANTE", "5": "PUNTO FIJO"}
            print(f"\n--- {nombres[opcion]} ---")
            
            if opcion == "3":
                # Newton-Raphson: un valor inicial
                x0 = float(input("Ingresa el valor inicial x0: "))
                tipo_error = solicitar_tipo_error()
                tolerancia = solicitar_tolerancia(tipo_error)
                newton_raphson(x0, tolerancia, tipo_error)
                
            elif opcion == "4":
                # Secante: dos valores iniciales
                x0 = float(input("Ingresa el primer valor inicial x0: "))
                x1 = float(input("Ingresa el segundo valor inicial x1: "))
                tipo_error = solicitar_tipo_error()
                tolerancia = solicitar_tolerancia(tipo_error)
                metodo_secante(x0, x1, tolerancia, tipo_error)
                
            elif opcion == "5":
                # Punto Fijo: un valor inicial
                x0 = float(input("Ingresa el valor inicial x0: "))
                tipo_error = solicitar_tipo_error()
                tolerancia = solicitar_tolerancia(tipo_error)
                punto_fijo(x0, tolerancia, tipo_error)
                
        else:
            print("Opcion invalida. Elegi un numero del 0 al 5.")
            
    except ValueError:
        print("Entrada invalida. Usa numeros.")
        return
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
        return
    except Exception as e:
        print(f"Error: {e}")
        return
        
    # Preguntar si quiere continuar
    continuar = input("\nQueres seguir probando con otro metodo? (s/n): ").strip().lower()
    if continuar in ['s', 'si', 'sí', 'y', 'yes']:
        print("\n" + "=" * 70)
        main()

if __name__ == "__main__":
    print("Sistema de metodos de localizacion de raices!")
    main()
