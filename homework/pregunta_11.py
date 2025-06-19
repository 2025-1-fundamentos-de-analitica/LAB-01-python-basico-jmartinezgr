"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contenga la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabéticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        lines = file.readlines()

    result = {}

    for line in lines:
        columns = line.strip().split("\t")
        if len(columns) > 3:
            valor = int(columns[1])
            letras = columns[3].split(",")  # separa letras individuales

            for letra in letras:
                if letra not in result:
                    result[letra] = 0
                result[letra] += valor

    return dict(sorted(result.items()))
