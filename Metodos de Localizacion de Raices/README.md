# METODOS DE LOCALIZACION DE RAICES

Sistema simple y directo para encontrar raices usando 5 metodos numericos.

## 🎯 Como Usar

### 1. Define tu funcion en `funciones.py`
```python
def f(x):
    return x**2 - 4  # <-- CAMBIA ESTA LINEA

def df_dx(x):
    return 2*x       # <-- CAMBIA ESTA LINEA (solo si usas Newton-Raphson)

def g(x):
    return 4/x       # <-- CAMBIA ESTA LINEA (solo si usas Punto Fijo)
```

### 2. Ejecuta el programa
```bash
python3 main.py
```

### 3. Elige tu metodo y listo!

## 📊 Metodos Disponibles

| Metodo | Que Necesitas | Velocidad |
|--------|---------------|-----------|
| **1. Biseccion** | Intervalo [a,b] | Lenta pero segura |
| **2. Regla Falsi** | Intervalo [a,b] | Mas rapida |
| **3. Newton-Raphson** | Valor inicial + derivada | Muy rapida |
| **4. Secante** | Dos valores iniciales | Rapida |
| **5. Punto Fijo** | Valor inicial + g(x) | Variable |

## 💡 Ejemplos de Funciones

### Cuadratica
```python
def f(x): return x**2 - 4        # Raices: ±2
def df_dx(x): return 2*x
```

### Trigonometrica  
```python
def f(x): return math.sin(x) - 0.5    # Raiz: π/6
def df_dx(x): return math.cos(x)
```

### Cubica
```python
def f(x): return x**3 - 2*x - 5       # Raiz: ~2.09
def df_dx(x): return 3*x**2 - 2
```

## ⚙️ Configuración de Error

- **Error Absoluto**: |x_nuevo - x_anterior|
- **Error Porcentual**: |x_nuevo - x_anterior| / |x_nuevo| × 100%

## 📈 Función de Prueba

Actualmente configurado para: **f(x) = x² - 4**
- Raíces: x = ±2
- El sistema busca la raíz positiva x = 2

## 🎯 Ejemplo de Uso

```python
from newton_raphson import newton_raphson

# Encontrar raíz con Newton-Raphson
newton_raphson(x0=3, tolerancia=1e-3, tipo_error='absoluto')
```

## 📝 Notas

- Para métodos de intervalo (Bisección, Regla Falsi): f(a) y f(b) deben tener signos opuestos
- Para métodos iterativos: elegir valores iniciales cerca de la raíz esperada
- Tolerancia recomendada: 1e-3 a 1e-6
