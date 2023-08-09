# Lectura de archivos de texto y CSV

"""La lectura de archivos de texto en Python es una tarea común en el procesamiento de datos y la manipulación de archivos. Python proporciona varias formas de leer archivos de texto, lo que nos permite acceder y utilizar la información contenida en ellos. Aquí tienes una descripción detallada de cómo leer archivos de texto en Python:

Abrir un archivo: Para leer un archivo de texto, primero debemos abrirlo en modo lectura utilizando la función open(). El modo de apertura debe establecerse como “r” o “rt” para archivos de texto.
file = open("archivo.txt", "r")
Leer todo el contenido: Una vez que hemos abierto el archivo, podemos leer todo su contenido utilizando el método read(). Este método devuelve una cadena que contiene todo el contenido del archivo.
content = file.read()
print(content)
Leer línea por línea: Si deseamos leer el contenido del archivo línea por línea, podemos utilizar el método readline(). Este método lee una línea a la vez y mueve el indicador de posición del archivo a la siguiente línea.
line = file.readline()
while line:
    print(line)
    line = file.readline()
Leer todas las líneas: Si queremos leer todas las líneas del archivo y almacenarlas en una lista, podemos utilizar el método readlines(). Este método devuelve una lista donde cada elemento es una línea del archivo.
lines = file.readlines()
for line in lines:
    print(line)
Cerrar el archivo: Después de leer el archivo, es importante cerrarlo utilizando el método close(). Esto libera los recursos asociados al archivo y garantiza que no se produzcan conflictos de acceso en futuras operaciones.
file.close()
Es importante tener en cuenta que la apertura y el cierre del archivo son operaciones necesarias para asegurar una manipulación adecuada de los archivos y evitar problemas de acceso o pérdida de datos.

Además, es una buena práctica utilizar bloques try-finally o with al leer archivos de texto. Estos bloques garantizan que el archivo se cierre correctamente, incluso si se produce una excepción durante el proceso de lectura.

try:
    file = open("archivo.txt", "r")
    # Realizar operaciones de lectura
finally:
    file.close()
O utilizando el bloque with:

with open("archivo.txt", "r") as file:
    # Realizar operaciones de lectura
Leer CSV
Además de leer archivos de texto en Python, también es común necesitar leer archivos CSV (Comma-Separated Values). Los archivos CSV contienen datos estructurados separados por comas, lo que los convierte en una forma popular de almacenar y compartir conjuntos de datos. Aquí te dejamos la forma de cómo leer archivos CSV en Python:

Importar el módulo csv: Antes de leer archivos CSV, debemos importar el módulo csv, que proporciona funciones y clases específicas para trabajar con este tipo de archivos.
import csv
Abrir el archivo CSV: Al igual que con los archivos de texto, debemos abrir el archivo CSV en modo lectura utilizando la función open(). Es importante especificar el modo de apertura como “r” o “rt” para archivos de texto.
with open('archivo.csv', 'r') as file:
    # Realizar operaciones de lectura del archivo CSV
Crear un objeto lector CSV: Para leer los datos del archivo CSV, necesitamos crear un objeto lector CSV utilizando la función reader() del módulo csv. Este objeto nos permitirá acceder a los datos fila por fila.
with open('archivo.csv', 'r') as file:
    csv_reader = csv.reader(file)
    # Realizar operaciones de lectura del archivo CSV
Leer filas del archivo CSV: Utilizando el objeto lector CSV, podemos leer las filas del archivo CSV una a una utilizando un bucle for. Cada fila se representa como una lista de valores correspondientes a cada columna del archivo CSV.
with open('archivo.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        # Acceder a los valores de cada columna en la fila
        print(row)
Leer datos en diccionarios: Si el archivo CSV tiene una fila de encabezado que contiene los nombres de las columnas, podemos leer los datos en forma de diccionarios utilizando un objeto lector CSV con el método DictReader(). Esto nos permite acceder a los valores utilizando los nombres de las columnas como claves.
with open('archivo.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Acceder a los valores utilizando los nombres de las columnas
        print(row['columna1'], row['columna2'])
Es importante tener en cuenta que los archivos CSV pueden tener diferentes delimitadores, como comas, punto y coma o tabulaciones. Si el archivo CSV utiliza un delimitador distinto de la coma, podemos especificarlo al crear el objeto lector CSV utilizando el parámetro delimiter.

Todo esto y más lo puedes aprender en el Curso de Python: Comprehensions, Funciones y Manejo de Errores"""