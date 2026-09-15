import re
import json

# Archivos de entrada y salida
leer_archivo = "analizar.txt"
escribir_archivo = "resultado.json"

# Diccionario de tokens con regex
especificacion_tokens = {
    'ESPACIO':      r'[ \t]+',
    'SALTO_LINEA':  r'[ \n]+',
    'COMENTARIO':   r'#.*',
    'ID':           r'[a-zA-Z]1[\w]*',
    'NUM':          r'[\d]+',
    'OP_EQUAL':     r'=',
    'OP_ADD':       r'[+]',
    'OP_SUB':       r'-',
    'OP_MULT':      r'[*]',
    'OP_DIV':       r'/',
    'OP_POT':       r'\^',
    'OP_ROOT':      r'\\',
    'PAR_OPEN':     r'[(]',
    'PAR_CLOSE':    r'[)]',
}

def analizar(codigo):
    tokens_lista = []
    linea = 1
    columna = 1
    pos = 0

    while pos < len(codigo):
        for tipo, patron in especificacion_tokens.items():
            coincidencia = re.match(patron, codigo[pos:])
            if coincidencia:
                valor = coincidencia.group()

                if tipo in ('ESPACIO', 'COMENTARIO', 'SALTO_LINEA'):
                    if '\n' in valor:
                        linea += valor.count('\n')
                        columna = len(valor) - valor.rfind('\n')
                    else:
                        columna += len(valor)
                else:
                    # Guardamos el token usando claves en minúscula como pediste
                    tokens_lista.append({
                        "type": tipo,
                        "value": valor,
                        "linea": linea,
                        "columna": columna
                    })
                    columna += len(valor)

                pos += len(valor)
                break
        else:
            # ESTO DETIENE EL ANALIZADOR SI HAY UN CARÁCTER INVÁLIDO
            raise SyntaxError(
                f"Carácter no reconocido {codigo[pos]!r} en línea {linea}, columna {columna}"
            )

    # Añadimos el End Of File
    tokens_lista.append({"type": "EOF", "value": None, "linea": linea, "columna": columna})

    # CONVERSIÓN AL FORMATO JSON DESEADO ("token1": {...}, "token2": {...})
    diccionario_salida = {}
    for indice, token in enumerate(tokens_lista, start=1):
        nombre_token = f"token{indice}"
        diccionario_salida[nombre_token] = token

    return diccionario_salida

def procesar_archivos():
    # 1. LEER EL ARCHIVO .TXT
    try:
        with open(leer_archivo, "r", encoding="utf-8") as archivo_txt:
            codigo_fuente = archivo_txt.read()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{leer_archivo}'.")
        return

    # 2. ANALIZAR EL CÓDIGO
    try:
        resultado = analizar(codigo_fuente)
    except SyntaxError as error:
        print(f"\nERROR LÉXICO: {error}")
        print("El análisis se ha detenido. No se generará el archivo JSON.\n")
        return # Detiene la ejecución para no crear el json si hay error

    # 3. ESCRIBIR EL ARCHIVO .JSON
    with open(escribir_archivo, "w", encoding="utf-8") as archivo_json:
        # json.dump escribe todo el diccionario de una vez con el formato correcto
        json.dump(resultado, archivo_json, indent=2, ensure_ascii=False)

    print(f"\nAnálisis exitoso. Los resultados se guardaron en '{escribir_archivo}'\n")

if __name__ == '__main__':
    procesar_archivos()