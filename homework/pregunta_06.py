"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        lines = file.readlines()

    result = {}
    for line in lines:
        columns = line.strip().split("\t")
        if len(columns) > 4:
            data_str = columns[4]
            pairs = data_str.split(",")
            for pair in pairs:
                key, value_str = pair.split(":")
                value = int(value_str)
                if key not in result:
                    result[key] = [value, value]  # [min, max]
                else:
                    result[key][0] = min(result[key][0], value)
                    result[key][1] = max(result[key][1], value)

    sorted_result = sorted((k, v[0], v[1]) for k, v in result.items())
    return sorted_result
