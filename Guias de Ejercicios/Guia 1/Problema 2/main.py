import matplotlib.pyplot as plt
import numpy as np
from biseccion_modificado import biseccion_con_historial
from regula_falsi_modificado import regula_falsi_con_historial

def main():
    print("=" * 80)
    print("PROBLEMA 2: COMPARACION DE METODOS NUMERICOS")
    print("Funcion: g(a) = a^10 - 1")
    print("=" * 80)
    
    # Parametros del problema
    a = 0.5  # Limite inferior del intervalo
    b = 1.5  # Limite superior del intervalo
    tolerancia = 1e-5
    tipo_error = 'absoluto'
    
    print(f"Intervalo de busqueda: [{a}, {b}]")
    print(f"Tolerancia requerida: {tolerancia}")
    print(f"Tipo de error: {tipo_error}")
    
    # Ejecutar metodo de biseccion
    print("\n" + "="*50)
    raiz_biseccion, errores_biseccion, iter_biseccion = biseccion_con_historial(
        a, b, tolerancia, tipo_error
    )
    
    # Ejecutar metodo de regla falsi
    print("\n" + "="*50)
    raiz_regla_falsi, errores_regla_falsi, iter_regla_falsi = regula_falsi_con_historial(
        a, b, tolerancia, tipo_error
    )
    
    # Resultados comparativos
    print("\n" + "="*80)
    print("RESULTADOS COMPARATIVOS")
    print("="*80)
    print(f"Biseccion:")
    print(f"  Raiz encontrada: {raiz_biseccion:.8f}")
    print(f"  Iteraciones: {len(iter_biseccion)}")
    print(f"  Error final: {errores_biseccion[-1]:.8f}" if errores_biseccion else "No disponible")
    
    print(f"\nRegla Falsi:")
    print(f"  Raiz encontrada: {raiz_regla_falsi:.8f}")
    print(f"  Iteraciones: {len(iter_regla_falsi)}")
    print(f"  Error final: {errores_regla_falsi[-1]:.8f}" if errores_regla_falsi else "No disponible")
    
    # Verificacion de las raices (deben ser aproximadamente 1)
    valor_teorico = 1.0
    print(f"\nVerificacion (valor teorico = {valor_teorico}):")
    if raiz_biseccion:
        print(f"Error absoluto Biseccion: {abs(raiz_biseccion - valor_teorico):.8f}")
    if raiz_regla_falsi:
        print(f"Error absoluto Regla Falsi: {abs(raiz_regla_falsi - valor_teorico):.8f}")
    
    # Generar graficos comparativos
    generar_graficos_comparativos(errores_biseccion, iter_biseccion, 
                                errores_regla_falsi, iter_regla_falsi)

def generar_graficos_comparativos(errores_bis, iter_bis, errores_rf, iter_rf):
    """Genera graficos comparativos de convergencia"""
    
    # Grafico 1: Comparacion de errores vs iteraciones (escala lineal)
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    if errores_bis and iter_bis:
        plt.plot(iter_bis, errores_bis, 'b-o', label='Biseccion', linewidth=2, markersize=4)
    if errores_rf and iter_rf:
        plt.plot(iter_rf, errores_rf, 'r-s', label='Regla Falsi', linewidth=2, markersize=4)
    
    plt.xlabel('Numero de Iteraciones')
    plt.ylabel('Error Absoluto')
    plt.title('Convergencia - Escala Lineal')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Grafico 2: Comparacion de errores vs iteraciones (escala logaritmica)
    plt.subplot(1, 2, 2)
    if errores_bis and iter_bis:
        plt.semilogy(iter_bis, errores_bis, 'b-o', label='Biseccion', linewidth=2, markersize=4)
    if errores_rf and iter_rf:
        plt.semilogy(iter_rf, errores_rf, 'r-s', label='Regla Falsi', linewidth=2, markersize=4)
    
    plt.xlabel('Numero de Iteraciones')
    plt.ylabel('Error Absoluto (escala log)')
    plt.title('Convergencia - Escala Logaritmica')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('comparacion_convergencia.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Grafico 3: Funcion g(a) = a^10 - 1
    plt.figure(figsize=(10, 6))
    x = np.linspace(0.3, 1.7, 1000)
    y = x**10 - 1
    
    plt.plot(x, y, 'k-', linewidth=2, label='g(a) = a^10 - 1')
    plt.axhline(y=0, color='gray', linestyle='--', alpha=0.7)
    plt.axvline(x=1, color='gray', linestyle='--', alpha=0.7)
    
    # Marcar las raices encontradas
    plt.plot(1, 0, 'go', markersize=8, label='Raiz teorica (a=1)')
    
    plt.xlabel('a')
    plt.ylabel('g(a)')
    plt.title('Funcion g(a) = a^10 - 1')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.xlim(0.3, 1.7)
    
    plt.savefig('funcion_grafica.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\nGraficos guardados:")
    print("- comparacion_convergencia.png: Comparacion de convergencia entre metodos")
    print("- funcion_grafica.png: Grafica de la funcion g(a) = a^10 - 1")

if __name__ == "__main__":
    main()