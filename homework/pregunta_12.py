"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        lines = file.readlines()

    result = {}

    for line in lines:
        columns = line.strip().split("\t")
        if len(columns) > 4:
            key = columns[0]
            value_str = columns[4]
            pairs = value_str.split(",")
            total_value = sum(int(pair.split(":")[1]) for pair in pairs)

            if key not in result:
                result[key] = 0
            result[key] += total_value

    return dict(sorted(result.items()))
