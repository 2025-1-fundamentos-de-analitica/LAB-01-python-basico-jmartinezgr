"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()

    count_dict = {}
    for line in lines:
        columns = line.strip().split("\t")
        if len(columns) > 0:
            first_letter = columns[0][0].upper()
            if first_letter in count_dict:
                count_dict[first_letter] += 1
            else:
                count_dict[first_letter] = 1

    sorted_counts = sorted(count_dict.items())
    return sorted_counts
