import re
import json

codigo = """x1das = 5 + 3 \n/ a1fk
X1 = 2"""

# Diccionario de tokens con regex
especificacion_tokens = {
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
    'OP_ROOT':    r'\\',                   #El doble backslash es para que Python lo interprete como un solo backslash, ya que el backslash es un caracter de escape, la r es para que Python lo interprete como un raw string, y no como un string normal
    'PAR_OPEN':   '[(]',
    'PAR_CLOSE':  '[)]',
}

def analizar(codigo):
    tokens = []
    linea = 1
    columna = 1
    pos = 0

    while pos < len(codigo):

        for tipo, patron in especificacion_tokens.items():
            coincidencia = re.match(patron, codigo[pos:])
            if coincidencia:
                valor = coincidencia.group()

                if tipo in ('ESPACIO', 'COMENTARIO', 'SALTO_LINEA'):
                    # Si capturamos un salto de línea, actualizamos el contador de líneas
                    if '\n' in valor:
                        linea += valor.count('\n')
                        # Reiniciamos la columna
                        columna = len(valor) - valor.rfind('\n')
                    else:
                        columna += len(valor)

                else:
                    # Si no es espacio ni salto ni comentario, SÍ es un token válido
                    tokens.append({
                        'Type': tipo,
                        'Value': valor,
                        'Line': linea,
                        'Col': columna
                    })
                    columna += len(valor)

                pos += len(valor)
                break
        else:
            raise SyntaxError(
                f"Carácter no reconocido {codigo[pos]!r} en línea {linea}, columna {columna}"
            )

    # El fin de archivo tambien es un token EOF
    tokens.append({'Type': 'EOF', 'Value': None, 'Line': linea, 'Col': columna})
    return tokens

# def read_file():
#     with open("analizar.txt", "r", encoding="utf-8") as archivo:
#         for numero_linea, linea in enumerate (archivo, start=1):
#             print(f"Análisis de linea {numero_linea}:")
#             resultado = analizar(codigo)
#             for token in resultado:
#                 print(token)

def write_file():
    with open("resultado.json", "w", encoding="utf-8") as archivo:
        for token in resultado:
            archivo.write(f"{token}\n")


if __name__ == '__main__':
    resultado = analizar(codigo)
    for token in resultado:
        print(token)
    # read_file()
    write_file()