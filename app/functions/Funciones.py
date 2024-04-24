import csv
import numpy as np
import re, random
import os
import math


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


def suma_total(conocimiento):
    """
    Suma los valores en cada columna del archivo csv.
    """
    sumas_filas = []

    for fila in conocimiento:
        suma_fila = sum(fila)
        sumas_filas.append(suma_fila)

    return sumas_filas


def obtenerIDF(df, conocimiento):
    return 0


def normalizar(conocimiento, total):
    """
    Normaliza cada valor en las filas de conocimiento dividiendo por la raíz cuadrada de la suma total de las filas.
    """
    # Calcular la raíz cuadrada de cada valor en total
    raices_cuadradas = [math.sqrt(valor) for valor in total]

    # Dividir cada elemento de las filas por la raíz cuadrada
    conocimiento_normalizado = []
    for fila, raiz_cuadrada in zip(conocimiento, raices_cuadradas):
        fila_normalizada = [valor / raiz_cuadrada for valor in fila]
        conocimiento_normalizado.append(fila_normalizada)

    return conocimiento_normalizado


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


def get_first_column(row_number):
    """
    Obtiene el valor de la primera columna de la fila con el número dado.
    """
    data = leerBase()
    if row_number < len(data):
        return data[row_number][0]
    else:
        return None


def get_all_column():
    """
    Function that returns the first column of the data returned by leerBase(), excluding the first row.
    """
    data = leerBase()
    first_column = [row[0] for row in data[1:]]  # Skip the first row
    return first_column


# intereses por atributo
def calculate_dot_product(random_vector, conocimiento):
    """
    Calculates the dot product between the random_vector and each column in the normalized conocimiento.
    """
    conocimiento_normalizado = normalizar(conocimiento, suma_total(conocimiento))
    conocimiento_transpose = np.transpose(conocimiento_normalizado)
    dot_products = [np.dot(random_vector, column) for column in conocimiento_transpose]
    return dot_products


# DF
def DF_Frecuency(conocimiento_normalizado):
    """
    Calculates the sum of non-zero attributes for each column in conocimiento_normalizado.
    """
    conocimiento_transpose = np.transpose(conocimiento_normalizado)
    attribute_sums = [
        sum(1 for value in column if value != 0) for column in conocimiento_transpose
    ]
    return attribute_sums


def IDF(attribute_sums, conocimiento_normalizado):
    """
    Calculates the IDF for each attribute.
    """
    totalproductos = len(conocimiento_normalizado)
    idf_values = [math.log(39 / df) if df != 0 else 0 for df in attribute_sums]
    return idf_values


def predictions(conocimiento_normalizado, idf_values, intereces_atributos):
    """
    Calculates the dot product of each row of conocimiento_normalizado with IDF and intereces_atributos vectors.
    """
    prediction_values = []  # Initialize an empty list to store the dot products

    for (
        row
    ) in conocimiento_normalizado:  # Iterate over each row in conocimiento_normalizado
        # Perform element multiplication of idf_values and intereces_atributos
        # This is necessary to multiply corresponding elements of both vectors
        multiplied_values = np.multiply(idf_values, intereces_atributos)

        # Calculate the dot product using NumPy's dot product function
        dot_product = np.dot(row, multiplied_values)

        # Append the dot product to the prediction_values list
        prediction_values.append(dot_product)

    return prediction_values  # Return the list of dot products


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
    random_vector = [random.choice([1, 0, -1]) for _ in range(39)]
    print(random_vector)
    conocimiento = obtenerDF(leerBase())
    total = suma_total(conocimiento)

    conocimiento_normalizado = normalizar(conocimiento, total)
    intereces_atributos = calculate_dot_product(random_vector, conocimiento_normalizado)
    attribute_sums = DF_Frecuency(conocimiento_normalizado)
    idf_values = IDF(attribute_sums, conocimiento_normalizado)

    prediction_values = predictions(
        conocimiento_normalizado, idf_values, intereces_atributos
    )
    print("====================================================")
    print(intereces_atributos)  # IpA
    print("====================================================")
    print(attribute_sums)  # DF
    print("====================================================")
    print(idf_values)  # IDF
    print("====================================================")
    print(prediction_values)
