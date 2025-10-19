# Metodos Numericos - Biblioteca Modularizada

Una biblioteca completa de metodos numericos implementados en Python puro, sin dependencias externas. Codigo limpio y simple, estilo estudiante de ingenieria.

## 🚀 Caracteristicas Principales

- **Localizacion de Raices**: Biseccion, Newton-Raphson, Regula Falsi, Punto Fijo, Secante
- **Sistemas Lineales**: Eliminacion Gaussiana, Jacobi, Gauss-Seidel, Metodo de Relajacion
- **Interpolacion**: Lagrange, Sistema de Ecuaciones, Spline Cubica, Cuadrados Minimos
- **Integracion Numerica**: Simpson Compuesta, Trapecio Compuesto, Estimacion de Errores
- **Diferenciacion Numerica**: Diferencias Finitas (adelante, atras, centradas) hasta 4ta derivada
- **Implementacion Pura**: Solo usa la biblioteca estandar de Python
- **Codigo Limpio**: Sin acentos, sin prints innecesarios, formato simple
- **Modularizacion**: Facil importacion y uso independiente de cada metodo

## 📦 Instalacion y Configuracion

### Instalacion Basica
```bash
# Clonar el repositorio
git clone <repository-url>
cd Metodos-Numericos

# No requiere instalacion de dependencias adicionales
# La biblioteca funciona con Python estandar
```

### Verificar Funcionalidad
```bash
# Probar ejercicios de examenes
cd examenes/parcial1
python ejercicio_01.py

# Probar metodos de integracion
python ejemplo_integracion.py

# Probar metodos de diferenciacion
python ejemplo_diferencias_finitas.py

# Probar modulos principales
python -c "from metodos_numericos import biseccion; print('OK')"
```

## 🔧 Uso Rapido

### Localizacion de Raices
```python
# Importar metodos especificos
from metodos_numericos.localizacion_raices import biseccion
from metodos_numericos.funciones import FuncionesBasicas

# Usar funcion predefinida
f = FuncionesBasicas.f2  # x^3 - 2x - 5

# Encontrar raiz
raiz, f_raiz, error = biseccion(f, 2, 3, tolerancia=1e-6)
print(f"Raiz: {raiz:.6f}, Error: {error:.2e}")
```

### Integracion Numerica
```python
# Importar metodos de integracion
from metodos_numericos.integracion import (
    trapecio_simple, trapecio_compuesto_v2, 
    simpson_1_3_simple, simpson_1_3_compuesto,
    gauss_legendre_integration
)

# Definir funcion
def f(x):
    return x**2 + 1

# Trapecio simple
resultado_trap = trapecio_simple(f, 0, 3)
print(f"Trapecio simple: {resultado_trap}")

# Simpson 1/3 simple (más preciso)
resultado_simp = simpson_1_3_simple(f, 0, 3)
print(f"Simpson 1/3: {resultado_simp}")

# Gauss-Legendre (alta precisión con pocas evaluaciones)
resultado_gauss = gauss_legendre_integration(f, 0, 3, n_points=4)
print(f"Gauss-Legendre (4 pts): {resultado_gauss}")
```

### Ecuaciones Diferenciales Ordinarias (EDOs)
```python
# Importar métodos para EDOs
from metodos_numericos.ecuaciones_diferenciales import (
    metodo_euler, metodo_heun, metodo_punto_medio,
    calcular_error_convergencia
)
import numpy as np

# Definir EDO: y' = -2xy con y(0) = 1
def f(x, y):
    return -2 * x * y

# Solución exacta: y(x) = e^(-x²)
def solucion_exacta(x):
    return np.exp(-x**2)

# Resolver con diferentes métodos
x_euler, y_euler = metodo_euler(f, 0, 1, 1, h=0.2)
x_heun, y_heun = metodo_heun(f, 0, 1, 1, h=0.2)
x_pm, y_pm = metodo_punto_medio(f, 0, 1, 1, h=0.2)

print(f"Euler: y(1) ≈ {y_euler[-1]:.6f}")
print(f"Heun: y(1) ≈ {y_heun[-1]:.6f}")
print(f"Punto Medio: y(1) ≈ {y_pm[-1]:.6f}")
print(f"Exacto: y(1) = {solucion_exacta(1):.6f}")

# Análisis de convergencia
pasos = [0.5, 0.25, 0.125, 0.0625]
errores = calcular_error_convergencia(f, 0, 1, 1, solucion_exacta, pasos)
for i, h in enumerate(pasos):
    print(f"h={h}: Error Euler={errores['euler'][i]:.6f}")
```

### Diferenciacion Numerica
```python
# Importar clase de diferencias finitas
from metodos_numericos.diferencias_finitas import DiferenciasFinitas, PrecisionLevel
import numpy as np

# Definir funcion
def f(x):
    return x**3 + 2*x**2 - 3*x + 1

# Crear puntos de evaluacion
x = np.linspace(0, 2, 11)

# Crear objeto de diferencias finitas
df_obj = DiferenciasFinitas(f, x)

# Calcular primera derivada centrada de alta precision
primera_derivada = df_obj.primera_derivada_centrada(PrecisionLevel.HIGH)
print(f"Primera derivada: {primera_derivada}")
```

## 📚 Estructura del Proyecto

```
metodos_numericos/
├── __init__.py              # Importaciones principales
├── funciones.py             # Funciones matematicas predefinidas
├── localizacion_raices.py   # Metodos para encontrar raices
├── sistemas_lineales.py     # Solucion de sistemas lineales
├── interpolacion.py         # Interpolacion y regresion
├── integracion.py           # Metodos de integracion numerica
├── diferencias_finitas.py   # Metodos de diferenciacion numerica
├── ecuaciones_diferenciales.py # Metodos para resolver EDOs
└── utilidades.py            # Utilidades y herramientas

examenes/                    # Ejercicios de examenes
├── parcial1/                # Ejercicios del primer parcial
├── parcial2/                # Ejercicios del segundo parcial
└── examen_final/            # Ejercicios del examen final

ejemplo_integracion_basica.py  # Ejemplo métodos básicos de integración
ejemplo_diferencias_finitas.py # Ejemplo de uso de diferenciación
```

## 🔍 Metodos Disponibles

### Localizacion de Raices
- `biseccion(f, a, b, tolerancia, max_iter)`
- `newton_raphson(f, df, x0, tolerancia, max_iter)`
- `regula_falsi(f, a, b, tolerancia, max_iter)`
- `punto_fijo(g, x0, tolerancia, max_iter)`
- `secante(f, x0, x1, tolerancia, max_iter)`

### Sistemas Lineales
- `eliminacion_gaussiana(A, b)`
- `jacobi(A, b, x0, tolerancia, max_iter)`
- `gauss_seidel(A, b, x0, tolerancia, max_iter)`
- `relajacion(A, b, x0, omega, tolerancia, max_iter)`

### Interpolacion
- `sistema_ecuaciones(x_vals, y_vals)` - Interpolacion polinomial
- `lagrange(x_vals, y_vals, x)` - Interpolacion de Lagrange
- `spline_cubica(x_vals, y_vals, x)` - Interpolacion spline
- `cuadrados_minimos(x_vals, y_vals, grado)` - Regresion

### Integracion Numerica
**Métodos Básicos:**
- `trapecio_simple(f, a, b)` - Trapecio con un solo intervalo
- `trapecio_compuesto_v2(f, a, b, n)` - Trapecio con múltiples subintervalos
- `trapecio_compuesto_datos(x_datos, y_datos)` - Trapecio para datos tabulados
- `simpson_1_3_simple(f, a, b)` - Simpson 1/3 con un intervalo
- `simpson_1_3_compuesto(f, a, b, n)` - Simpson 1/3 con múltiples subintervalos

**Métodos Avanzados:**
- `simpson_compuesta_funcion(f, a, b, n)` - Simpson con función analítica
- `simpson_compuesta_datos(x_datos, y_datos)` - Simpson con datos tabulados  
- `simpson_compuesta_mejorada(f, a, b, n)` - Simpson con estimación de error
- `trapecio_compuesto(f, a, b, n)` - Implementación alternativa del trapecio
- `gauss_legendre_integration(f, a, b, n_points)` - Cuadratura de Gauss-Legendre (2-6 puntos)

**Cálculo de Errores:**
- `calcular_error_trapecio(f_segunda, a, b, c)` - Error teórico del trapecio
- `calcular_error_simpson(f_cuarta, a, b, c)` - Error teórico de Simpson

### Diferenciacion Numerica (Diferencias Finitas)
- `DiferenciasFinitas(f, x, h)` - Clase principal para calcular derivadas
- `primera_derivada_adelante/atras/centrada(precision)` - Primera derivada
- `segunda_derivada_adelante/atras/centrada(precision)` - Segunda derivada  
- `tercera_derivada_adelante/atras/centrada(precision)` - Tercera derivada
- `cuarta_derivada_adelante/atras/centrada(precision)` - Cuarta derivada
- `PrecisionLevel.LOW/HIGH` - Niveles de precision (menos/mas puntos)

### Ecuaciones Diferenciales Ordinarias (EDOs)
**Métodos Básicos:**
- `metodo_euler(f, x0, xf, y0, h, n)` - Método de Euler (orden 1)
- `metodo_heun(f, x0, xf, y0, h, n)` - Método de Heun/Euler mejorado (orden 2)
- `metodo_punto_medio(f, x0, xf, y0, h, n)` - Método del punto medio (orden 2)

**Análisis:**
- `calcular_error_convergencia(f, x0, xf, y0, solucion_exacta, pasos)` - Análisis de convergencia

## ⚙️ Dependencias

**Biblioteca Principal**: Solo biblioteca estandar de Python
- Sin dependencias externas requeridas
- Implementacion desde cero de todos los algoritmos
- Codigo limpio sin acentos ni caracteres especiales

**Opcionales** (para ejercicios especificos):
- `matplotlib`: Para graficos y visualizacion
- `numpy`: Para operaciones matematicas avanzadas y diferencias finitas

## � Estado del Proyecto

**Version**: 1.0.0 (Limpieza Completa)  
**Ultima Actualizacion**: Septiembre 2025

## �📄 Licencia

Este proyecto esta bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

