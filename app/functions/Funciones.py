import numpy as np
import re, random
import os


def leerBase():
    """
    Funcion que leer una base de conocimiento y la transforma en un arreglo de filas
    """
    datos = []

    # Obtener la ruta del directorio actual del script
    current_directory = os.path.dirname(__file__)

    # Construir la ruta al archivo CSV
    csv_file_path = os.path.join(current_directory, "IA-Recomendaciones.csv")

    # Abrir el archivo CSV
    archivo = open(csv_file_path, "r")

    try:
        next(archivo)
        for linea in archivo:
            aux = linea.rstrip("\n")
            newLinea = aux.split(",")
            datos.append(newLinea)
    finally:
        archivo.close()

    return datos

    """
    Funcion que leer una base de conocimiento y la transforma en un arreglo de filas
    """
    datos = []
    archivo = open(
        "IA-Recomendaciones.csv", "r"
    )  # Reemplaza 'nombre_archivo.txt' con la ruta y nombre de tu archivo
    try:
        next(archivo)
        for linea in archivo:
            aux = linea.rstrip("\n")
            newLinea = aux.split(",")
            datos.append(newLinea)
    finally:
        archivo.close()
    return datos


def cabeceras():
    """
    Funcion que regresa la primera columna de un archivo de conocimiento.
    """
    archivo = open(
        "IA-Recomendaciones.csv", "r"
    )  # Reemplaza 'nombre_archivo.txt' con la ruta y nombre de tu archivo
    try:
        aux = archivo.readline().rstrip("\n").split(",")
        aux = aux[1:]
    finally:
        archivo.close()
    # print(aux)
    return aux


def obtenerDF(conocimiento):
    """
    Lee el archivo CSV pasado como conocimiento y devuelve los datos como una lista de vectores,
    eliminando la primera fila y columna que contienen los títulos.
    """
    # Eliminar la primera columna del conocimiento (títulos)
    for i in range(len(conocimiento)):
        conocimiento[i] = [int(x) for x in conocimiento[i][1:]]
    return conocimiento


def obtenerIDF(df, conocimiento):
    return 0


def normalizar(conocimiento, total):
    return conocimiento


def matchUserInput(preferencia, c):
    pref = []
    for text in c:
        found = False
        for r in preferencia:
            if r.strip().lower() == text.strip().lower():
                # print("MATCH:", r)
                pref.append(1)
                found = True
                break
        if not found:
            pref.append(0)
    return pref


def matchPreference(preferencia, conocimiento):
    """
    Calcula la similitud entre el vector preferencia y los vectores en el conocimiento
    y devuelve el vector más cercano a preferencia, junto con su índice.
    """
    # LINEA QUE AGREGO ROGER XDXD
    conocimiento = obtenerDF(leerBase())

    # Convertir preferencia a un array de numpy
    preferencia = np.array(preferencia)

    # Calcular la distancia euclidiana entre preferencia y cada vector en el conocimiento
    distancias = np.linalg.norm(conocimiento - preferencia, axis=1)

    # Encontrar el índice del vector más cercano
    indice_minimo = np.argmin(distancias)
    # Obtener el vector más cercano
    vector_recomendado = conocimiento[indice_minimo]

    # Imprimir el índice del vector
    print("Índice del vector más cercano:", indice_minimo)
    print(get_first_column(indice_minimo))

    # return vector_recomendado cambio by roger xd
    return get_first_column(indice_minimo)


def get_first_column(row_number):
    """
    Obtiene el valor de la primera columna de la fila con el número dado.
    """
    data = leerBase()
    if row_number < len(data):
        return data[row_number][0]
    else:
        return None


if __name__ == "__main__":
    # print(leerBase())
    # print(cabeceras())
    preferencia = [
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        1,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        1,
        1,
        1,
        0,
        1,
        1,
        0,
    ]
    conocimiento = obtenerDF(leerBase())
    # print(conocimiento)
    matchPreference(preferencia, conocimiento)
