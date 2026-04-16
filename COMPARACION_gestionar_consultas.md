# COMPARACIÓN DETALLADA: gestionar_consultas.py
## Código Actual vs Refactorizado

---

## 1. IMPORTACIONES

**Actual:**
```python
from gestionar_json import *
from validaciones import validar_menu, validar_entero
from gestionar_herramienta import listar_herramienta
```

**Refactorizado:**
```python
from collections import Counter
from gestionar_json import cargar, guardar
from validaciones import validar_menu, validar_entero
```

**Diferencias:**
- Refactorizado usa `from collections import Counter` (más eficiente para contar)
- Refactorizado especifica importaciones explícitas en lugar de `*`
- Actual importa `listar_herramienta` que no se usa
- Refactorizado solo importa lo necesario

---

## 2. FUNCIONES AUXILIARES (NUEVAS EN REFACTORIZADO)

**Refactorizado agrega:**
```python
def _imprimir_herramienta(elemento):
    # Imprime formato estandarizado de herramienta
    
def _imprimir_prestamo(elemento):
    # Imprime formato estandarizado de préstamo
```

**Beneficios:**
- Evita duplicación de código (el actual repite esta estructura 3 veces)
- Más mantenible
- Mejora legibilidad

---

## 3. FUNCIÓN: stock_minimo()

### **Estructura y Flujo**

**Actual:**
```
- Carga registros
- if not registros: print mensaje
- else: pide stock, ITERA TODOS con for, 
  IMPRIME dentro del loop y RETORNA en la primera coincidencia
- Luego imprime "NO SE ENCONTRÓ"
```

**Refactorizado:**
```
- Carga registros
- if not registros: print y return (temprana)
- Pide stock
- Crea lista con list comprehension: encontrados = [...]
- if not encontrados: print y return
- ITERA y IMPRIME todo lo encontrado
```

### **Diferencia Crítica: LÓGICA DEL RETURN**

**Actual:** `return` está DENTRO del loop → **Retorna después de IMPRIMIR EL PRIMERO**
```python
for elemento in registros:
    if elemento.get('cantidad', 'clave no encontrada') <= stock:
        print(...)  # Imprime el primero
        return      # ¡¡¡ SALE DEL BUCLE !!!
print('NO SE ENCONTRÓ...')  # Nunca se ejecuta si hay al menos una coincidencia
```

**Refactorizado:** Itera TODOS los resultados
```python
for elemento in encontrados:
    _imprimir_herramienta(elemento)  # Imprime TODOS
```

### **Diferencias en Manejo de Errores**

**Actual:**
- `elemento.get('cantidad', 'clave no encontrada') <= stock` 
  → Puede fallar si devuelve string en lugar de número

**Refactorizado:**
- `e.get('cantidad', 0) <= stock` 
  → Valor por defecto numérico (0)

### **Mensajes**

**Actual:** 
- Inicio: `'No se puede buscar porque no hay registros'`
- Final: `'NO SE ENCONTRÓ NINGÚN STOCK CON ESA CANTIDAD MINIMA: ', stock`

**Refactorizado:**
- Inicio: `'No hay herramientas registradas.'`
- Final: `f'No hay herramientas con stock menor o igual a {stock}.'`

---

## 4. FUNCIÓN: activos_completados()

### **Estructura de Control**

**Actual:**
- Usa `match-case` (Python 3.10+)
- **PROBLEMA CRÍTICO:** Los prints "NO SE ENCONTRO..." están DENTRO del if/else
  → Imprime el mensaje CADA VEZ que recorre un elemento que NO coincide

**Refactorizado:**
- Usa `if-else` simple
- Usa list comprehension para filtrar PRIMERO
- LUEGO imprime un solo mensaje si está vacío
- Itera todos los resultados

### **Lógica del Actual (INCORRECTO)**

```python
case 1:
    for elemento in registros:
        if elemento.get('estado') == 'En proceso':
            print(...)
        else:
            print('NO SE ENCONTRO...')  # ¡¡¡ IMPRIME POR CADA ELEMENTO QUE NO COINCIDE !!!
```

**Resultado esperado:** 2 préstamos "En proceso"
**Resultado actual:** 2 líneas de detalles + N-2 líneas "NO SE ENCONTRO..."

### **Lógica del Refactorizado (CORRECTO)**

```python
resultados = [e for e in registros if e.get('estado') == 'En proceso']
if not resultados:
    print(mensaje_vacio)
    return
for elemento in resultados:
    _imprimir_prestamo(elemento)
```

**Resultado esperado:** 2 líneas de detalles
**Resultado actual:** 2 líneas de detalles ✓

---

## 5. FUNCIÓN: historial_usuarios()

### **Estructura**

**Actual:**
- Loop sobre TODOS los registros buscando coincidencia
- Nunca maneja el caso "no encontrado"

**Refactorizado:**
- List comprehension filtra primero
- Manejo explícito si no hay resultados
- Mensaje específico con ID buscado

### **Mensajes**

**Actual:**
- `'No hay registros en este momento'`
- Sin mensaje si no hay coincidencias

**Refactorizado:**
- `'No hay préstamos registrados.'`
- `f'No se encontraron préstamos para el usuario con ID {id_usuario}.'`

---

## 6. FUNCIÓN: herramienta_mas_usada()

### **Algoritmo**

**Actual:**
```
1. Carga herramientas
2. Carga préstamos
3. Por cada herramienta:
   - Cuenta cuántos préstamos coinciden (BÚSQUEDA LINEAL)
   - Si > 0, añade a lista
4. Imprime lista formateada
```
**Complejidad:** O(n * m) donde n=herramientas, m=préstamos

**Refactorizado:**
```
1. Carga préstamos
2. Usa Counter para contar IDs de herramientas (UNA PASADA)
3. Carga herramientas
4. Por cada herramienta, consulta Counter
5. Si > 0, imprime directamente
```
**Complejidad:** O(n + m) - más eficiente

### **Diferencias Técnicas**

**Actual:**
```python
for i_herramientas in herramientas_list:
    contador=0
    for i_prestamos in registros:  # ¡¡¡ BUCLE ANIDADO !!!
        if i_herramientas['id'] == i_prestamos['herramienta']['id']:
            contador+=1
```

**Refactorizado:**
```python
conteo = Counter(p['herramienta']['id'] for p in registros if 'herramienta' in p)
# Counter ya tiene todo contado eficientemente
```

### **Formato de Salida**

**Actual:** `'1, Martillo = 5\n'` (con ID al inicio y = separador)

**Refactorizado:** `"1 - Martillo: 5 préstamo(s)"` (más legible)

---

## 7. FUNCIÓN: usuario_mas_usado()

### **Mismos Problemas que herramienta_mas_usada()**

**Actual:**
- Bucle anidado innecesario → O(n * m)
- Formato menos legible

**Refactorizado:**
- Usa Counter → O(n + m)
- Formato: `"1 - Juan Pérez: 5 préstamo(s)"`

---

## RESUMEN DE MEJORAS

| Aspecto | Actual | Refactorizado |
|---------|--------|----------------|
| **Duplicación de código** | Sí (3 bloques print idénticos) | No (funciones auxiliares) |
| **Eficiencia algorithmic** | O(n*m) en conteos | O(n+m) con Counter |
| **Lógica de filtrado** | Loops + condiciones anidadas | List comprehensions |
| **Manejo de casos vacíos** | Incompleto | Completo |
| **Bugs/Problemas** | 2-3 bugs lógicos serios | Ninguno |
| **Legibilidad de código** | Media | Alta |
| **Mensajes de error** | Genéricos | Descriptivos |
| **Manejo de None/Missing** | Arriesgado | Seguro con .get() |

---

## BUGS CRÍTICOS EN CÓDIGO ACTUAL

1. **stock_minimo():** Retorna después del primer resultado
2. **activos_completados():** Imprime "NO SE ENCONTRÓ" múltiples veces
3. **herramienta_mas_usada():** O(n*m) ineficiente
4. **usuario_mas_usado():** O(n*m) ineficiente
5. **Manejo de diccionarios:** `.get('clave erronea')` sin valor por defecto
