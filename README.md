# Metodos Numericos - Biblioteca Modularizada

Una biblioteca completa de metodos numericos implementados en Python puro, sin dependencias externas. Codigo limpio y simple, estilo estudiante de ingenieria.

## 🚀 Caracteristicas Principales

- **Localizacion de Raices**: Biseccion, Newton-Raphson, Regula Falsi, Punto Fijo, Secante
- **Sistemas Lineales**: Eliminacion Gaussiana, Jacobi, Gauss-Seidel, Metodo de Relajacion
- **Interpolacion**: Lagrange, Sistema de Ecuaciones, Spline Cubica, Cuadrados Minimos
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

# Probar modulos principales
python -c "from metodos_numericos import biseccion; print('OK')"
```

## 🔧 Uso Rapido

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

## 📚 Estructura del Proyecto

```
metodos_numericos/
├── __init__.py              # Importaciones principales
├── funciones.py             # Funciones matematicas predefinidas
├── localizacion_raices.py   # Metodos para encontrar raices
├── sistemas_lineales.py     # Solucion de sistemas lineales
├── interpolacion.py         # Interpolacion y regresion
└── utilidades.py            # Utilidades y herramientas

examenes/                    # Ejercicios de examenes
├── parcial1/                # Ejercicios del primer parcial
├── parcial2/                # Ejercicios del segundo parcial
└── examen_final/            # Ejercicios del examen final
```

## 🧪 Ejemplos de Uso

### Ejecutar Ejercicios de Examenes
```bash
# Ejemplo: Parcial 1, Ejercicio 1
cd examenes/parcial1
python ejercicio_01.py

# Ejemplo: Parcial 2, Ejercicio 2
cd examenes/parcial2
python ejercicio_02.py
```

### Importar en Codigo Propio
```python
# Ejemplo completo de uso
from metodos_numericos.localizacion_raices import newton_raphson

# Definir funcion y su derivada
f = lambda x: x**3 - 2*x - 5
df = lambda x: 3*x**2 - 2

# Encontrar raiz con Newton-Raphson
raiz, f_raiz, error = newton_raphson(f, df, x0=2, tolerancia=1e-8)
print(f"Raiz encontrada: {raiz:.8f}")
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

## ⚙️ Dependencias

**Biblioteca Principal**: Solo biblioteca estandar de Python
- Sin dependencias externas requeridas
- Implementacion desde cero de todos los algoritmos
- Codigo limpio sin acentos ni caracteres especiales

**Opcionales** (para ejercicios especificos):
- `matplotlib`: Para graficos y visualizacion
- `numpy`: Para operaciones matematicas avanzadas

## 🚀 Caracteristicas Tecnicas

- ✅ **Sin dependencias**: Funciona con Python puro
- ✅ **Modular**: Cada metodo es independiente
- ✅ **Codigo limpio**: Sin acentos, prints minimos, formato simple
- ✅ **Probado**: Ejercicios validados y funcionales
- ✅ **Educativo**: Ideal para aprendizaje de metodos numericos
- ✅ **Estilo estudiante**: Codigo directo y sin decoraciones

## � Estado del Proyecto

**Version**: 1.0.0 (Limpieza Completa)  
**Ultima Actualizacion**: Septiembre 2025

### ✅ Cambios Recientes:
- Eliminacion completa de acentos y enes
- Simplificacion de prints y mensajes de salida
- Correccion de caracteres especiales (\\n visibles)
- Formato de codigo estilo estudiante de ingenieria
- Verificacion de funcionamiento de todos los ejercicios

### 📁 Archivos Principales:
- `examenes/parcial1/` - Ejercicios verificados y funcionales
- `examenes/parcial2/` - Ejercicios verificados y funcionales  
- `metodos_numericos/` - Modulos principales limpios y funcionales

## �📄 Licencia

Este proyecto esta bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

