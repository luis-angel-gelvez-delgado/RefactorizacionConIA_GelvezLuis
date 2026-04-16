"""
Comparación de salidas: gestionar_consultas actual vs refactorizado
"""

print("=" * 80)
print("COMPARACIÓN DE RESULTADOS")
print("=" * 80)

print("\n" + "=" * 80)
print("1. FUNCIÓN: stock_minimo()")
print("=" * 80)

# Simulamos los datos
herramientas = [
    {'id': 1, 'nombre': 'Martillo', 'cantidad': 5, 'estado': 'Activa', 'precio': 25.00},
    {'id': 2, 'nombre': 'Destornillador', 'cantidad': 2, 'estado': 'Activa', 'precio': 10.00},
    {'id': 3, 'nombre': 'Llave inglesa', 'cantidad': 1, 'estado': 'Activa', 'precio': 15.00},
    {'id': 4, 'nombre': 'Taladro', 'cantidad': 8, 'estado': 'Activa', 'precio': 50.00},
]

stock_minimo_buscado = 3

print(f"\nBuscando herramientas con stock <= {stock_minimo_buscado}")
print("\nCÓDIGO ACTUAL - Busca y retorna en PRIMER resultado:")
print("-" * 80)
for elemento in herramientas:
    if elemento.get('cantidad') <= stock_minimo_buscado:
        print(f"Encontrado: ID={elemento['id']}, Nombre={elemento['nombre']}, Cantidad={elemento['cantidad']}")
        print("✗ [RETORNA AQUÍ - NO MUESTRA LOS OTROS 2 RESULTADOS]")
        break
print("\nREAL: Solo muestra 1 resultado (INCORRECTO)")

print("\nCÓDIGO REFACTORIZADO - Filtra TODOS y luego imprime:")
print("-" * 80)
encontrados = [e for e in herramientas if e.get('cantidad', 0) <= stock_minimo_buscado]
if encontrados:
    for elemento in encontrados:
        print(f"Encontrado: ID={elemento['id']}, Nombre={elemento['nombre']}, Cantidad={elemento['cantidad']}")
    print(f"\nTotal encontrados: {len(encontrados)} (CORRECTO)")
else:
    print(f"No hay herramientas con stock menor o igual a {stock_minimo_buscado}.")

print("\n" + "=" * 80)
print("2. FUNCIÓN: activos_completados()")
print("=" * 80)

prestamos = [
    {'id': 1, 'usuario': {'id': 101, 'nombre': 'Juan'}, 'herramienta': {'id': 1, 'nombre': 'Martillo'}, 'estado': 'En proceso'},
    {'id': 2, 'usuario': {'id': 102, 'nombre': 'María'}, 'herramienta': {'id': 2, 'nombre': 'Destornillador'}, 'estado': 'Aceptada'},
    {'id': 3, 'usuario': {'id': 103, 'nombre': 'Carlos'}, 'herramienta': {'id': 3, 'nombre': 'Llave'}, 'estado': 'En proceso'},
    {'id': 4, 'usuario': {'id': 104, 'nombre': 'Ana'}, 'herramienta': {'id': 1, 'nombre': 'Martillo'}, 'estado': 'Rechazada'},
]

print("\nBuscando préstamos 'En proceso':")
print("\nCÓDIGO ACTUAL - Bucle con if/else (IMPRIME MENSAJE POR CADA NO-COINCIDENCIA):")
print("-" * 80)
encontrados_actual = 0
for elemento in prestamos:
    if elemento.get('estado') == 'En proceso':
        print(f"Préstamo ID={elemento['id']}: {elemento['usuario']['nombre']} - Estado: En proceso ✓")
        encontrados_actual += 1
    else:
        print(f"No coincide: ID={elemento['id']} - Estado: {elemento['estado']} ✗")

print(f"\n✗ PROBLEMA: Imprime {len(prestamos)} líneas (1 correcta + {len(prestamos)-encontrados_actual} mensajes incorrectos)")

print("\nCÓDIGO REFACTORIZADO - Filtra PRIMERO, valida resultado vacío, imprime después:")
print("-" * 80)
resultados = [e for e in prestamos if e.get('estado') == 'En proceso']
if not resultados:
    print("No hay préstamos en estado 'En proceso'.")
else:
    for elemento in resultados:
        print(f"Préstamo ID={elemento['id']}: {elemento['usuario']['nombre']} - Estado: En proceso ✓")
    print(f"\n✓ CORRECTO: Imprime solo {len(resultados)} línea(s) relevante(s)")

print("\n" + "=" * 80)
print("3. FUNCIÓN: herramienta_mas_usada()")
print("=" * 80)

print("\nCÓDIGO ACTUAL - Bucle anidado O(n*m):")
print("-" * 80)

# Contador manual simulando el actual
herramientas_conteo_actual = []
for herr in herramientas:
    contador = 0
    for prest in prestamos:
        if herr['id'] == prest['herramienta']['id']:
            contador += 1
    if contador > 0:
        herramientas_conteo_actual.append((herr['id'], herr['nombre'], contador))

for h_id, h_nombre, cantidad in herramientas_conteo_actual:
    print(f"{h_id}, {h_nombre} = {cantidad}")

print(f"Iteraciones: {len(herramientas)} herramientas × {len(prestamos)} préstamos = {len(herramientas) * len(prestamos)} comparaciones")

print("\nCÓDIGO REFACTORIZADO - Counter O(n+m):")
print("-" * 80)

from collections import Counter
conteo = Counter(p['herramienta']['id'] for p in prestamos if 'herramienta' in p)
for herr in herramientas:
    cantidad = conteo.get(herr['id'], 0)
    if cantidad > 0:
        print(f"{herr['id']} - {herr['nombre']}: {cantidad} préstamo(s)")

print(f"Iteraciones: {len(prestamos)} préstamos (contador) + {len(herramientas)} herramientas = {len(prestamos) + len(herramientas)} total")

print("\n✓ COMPARACIÓN:")
print(f"  - Actual: {len(herramientas) * len(prestamos)} comparaciones")
print(f"  - Refactorizado: {len(prestamos) + len(herramientas)} comparaciones")
print(f"  - Mejora: {(len(herramientas) * len(prestamos)) / (len(prestamos) + len(herramientas)):.1f}x más rápido")

print("\n" + "=" * 80)
print("RESUMEN DE DIFERENCIAS CRÍTICAS")
print("=" * 80)

tabla = """
┌────────────────────┬──────────────────────┬──────────────────────┐
│ Función            │ Código Actual         │ Refactorizado        │
├────────────────────┼──────────────────────┼──────────────────────┤
│ stock_minimo       │ Retorna 1er resultado │ Retorna todos        │
│ activos_completados│ Mensajes duplicados  │ Mensaje único        │
│ herramienta_usada  │ O(n*m) - lento       │ O(n+m) - rápido      │
│ usuario_usado      │ O(n*m) - lento       │ O(n+m) - rápido      │
└────────────────────┴──────────────────────┴──────────────────────┘
"""
print(tabla)
