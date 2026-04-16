import transformaciones as current
import transformaciones_refactored as refactored

print("Comparación de funciones:")
print()

# transformar_estado
print("transformar_estado(1):")
print(f"Actual: {current.transformar_estado(1)}")
print(f"Refactorizado: {refactored.transformar_estado(1)}")
print()

print("transformar_estado(2):")
print(f"Actual: {current.transformar_estado(2)}")
print(f"Refactorizado: {refactored.transformar_estado(2)}")
print()

print("transformar_estado(3):")
print(f"Actual: {current.transformar_estado(3)}")
print(f"Refactorizado: {refactored.transformar_estado(3)}")
print()

# transformar_tipo
print("transformar_tipo(1):")
print(f"Actual: {current.transformar_tipo(1)}")
print(f"Refactorizado: {refactored.transformar_tipo(1)}")
print()

print("transformar_tipo(2):")
print(f"Actual: {current.transformar_tipo(2)}")
print(f"Refactorizado: {refactored.transformar_tipo(2)}")
print()

# For gestionar and rechazar, we need sample data
# But since they modify json and print, perhaps just note the differences in code

print("Diferencias en gestionar:")
print("- Mensajes de impresión diferentes")
print("- Código refactorizado tiene función auxiliar _hay_stock_suficiente")
print("- Código refactorizado tiene return al final")
print()

print("Diferencias en rechazar:")
print("- Mensaje de prompt diferente")
print("- Código refactorizado usa parámetros en validar_texto")
print()

print("Diferencias en solicitar_fecha_inicio:")
print("- Código actual no valida la fecha (puede crear fechas inválidas)")
print("- Código refactorizado valida con try-except y loop hasta fecha válida")