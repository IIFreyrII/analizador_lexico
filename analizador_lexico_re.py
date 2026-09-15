import re
import json

#leer codigo
archivo = open('entrada.txt', 'r')
codigo = archivo.read()
archivo.close()

# codigo = """das = 5 + 3 / fk
# X = 2"""

# Diccionario de tokens con regex
especificacion_tokens = {
    'ESPACIO':      '[ \t]+',               #Así se especifican espaciones según la documentación de Python, el + es para que acepte 1 o más veces
    'COMENTARIO':    '#.*',                 #El punto es para que acepte cualquier caracter, y el asterisco es para que acepte 0 o más veces después del sharp
    'SALTO':      '\n',
    'ID':         r'[a-zA-Z][a-zA-Z0-9]*',
    'NUM':        r'[0-9]+(?![a-zA-Z0-9])',
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

                if tipo in ('ESPACIO', 'COMENTARIO'):
                    # Se ignoran
                    columna += len(valor)

                elif tipo in 'SALTO':
                    linea += 1
                    columna = 1

                else:
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

# guardar resultado
resultado = analizar(codigo)
with open('resultadocorrec', 'w') as archivo:
    json.dump(resultado, archivo)
archivo.close()

# if __name__ == '__main__':
#    resultado = analizar(codigo)
#    for token in resultado:
#        print(token)