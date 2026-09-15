import re
import json

# Diccionario de tokens con regex
tokens = {
    'ESPACIO':      '[ \t]+',               #Así se especifican espaciones según la documentación de Python, el + es para que acepte 1 o más veces
    'SALTO_LINEA':  '[ \n]+',               #Así se especifican saltos de línea según la documentación de Python, el + es para que acepte 1 o más veces
    'COMENTARIO':    '#.*',                 #El punto es para que acepte cualquier caracter, y el asterisco es para que acepte 0 o más veces después del sharp
    'ID':         r'[a-zA-Z]1[a-zA-Z0-9]*',
    'NUM':        r'[\d]+',
    'OP_EQUAL':   '=',
    'OP_ADD':     '[+]',
    'OP_SUB':     '-',
    'OP_MULT':    '[*]',
    'OP_DIV':     '/',
    'OP_POT':     r'\^',
    'OP_ROOT':    r'\\',
    'PAR_OPEN':   '[(]',
    'PAR_CLOSE':  '[)]',
}

leer_archivo = "analizar.txt"
escribir_archivo = "resultado.json"

# def read_file():
#     with open(leer_archivo, "r") as archivo_txt:
#         for numero_linea, linea in enumerate (archivo_txt, start=1):
#             print(f"Análisis de linea {numero_linea}:")
#             resultado = analizar(codigo)

salida = tokens
def write_file():
    with open(escribir_archivo, "w") as archivo_json:
        json.dump(salida, archivo_json, indent=2)

if __name__ == '__main__':
    # read_file()
    # write_file()
    print('Hello world')