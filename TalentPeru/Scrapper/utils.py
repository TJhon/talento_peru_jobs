# utils.py
def job_wage_float(wage: str):
    # 'S/. 1,950.00' -> 1950.00
    wage = wage.replace(",", "").replace("S/.").strip()
    return float(wage)


import re


def limpiar_espacios(texto):
    # Eliminar tabulaciones y reemplazarlas con un solo espacio
    texto = re.sub(r"\s{2,}", " ", texto)
    texto = re.sub(r"\t+", " ", texto)
    texto = re.sub(r"\n+", " ", texto)
    # Eliminar múltiples espacios (más de 2) y reemplazarlos con un solo espacio
    # Eliminar espacios al principio y al final
    return texto.strip()


def total_numbers(texto):
    # Expresión regular para encontrar secuencias de dígitos
    numeros = re.findall(r"\d+", texto)
    # Convertir los números encontrados a enteros
    return [int(num) for num in numeros]
