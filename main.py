spanish_c_keywords = {

    # Types
    "vacio": "void",
    "entero": "int",
    "caracter": "char",
    "flotante": "float",
    "doble": "double",
    "largo": "long",
    "corto": "short",
    "firmado": "signed",
    "sin_signo": "unsigned",

    # Control flow
    "si": "if",
    "sino": "else",
    "mientras": "while",
    "hacer": "do",
    "para": "for",
    "retornar": "return",
    "romper": "break",
    "continuar": "continue",

    # Switch
    "seleccionar": "switch",
    "caso": "case",
    "predeterminado": "default",

    # Storage classes
    "automatico": "auto",
    "registro": "register",
    "estatico": "static",
    "externo": "extern",

    # Constants / qualifiers
    "constante": "const",
    "volatil": "volatile",
    "restringido": "restrict",
    "en_linea": "inline",

    # Compound types
    "estructura": "struct",
    "union": "union",
    "enumeracion": "enum",
    "typedef": "typedef",

    # Boolean (C99/C23 style)
    "verdadero": "true",
    "falso": "false",

    # Null
    "nulo": "NULL",

    # C11/C23 keywords
    "alinear": "_Alignas",
    "alineacion": "_Alignof",
    "atomo": "_Atomic",
    "sin_retorno": "_Noreturn",
    "estatico_assert": "_Static_assert",
    "hilo_local": "_Thread_local",

    # Preprocessor-like words
    "incluir": "include",
    "definir": "define",
    "si_definido": "ifdef",
    "si_no_definido": "ifndef",
    "fin_si": "endif",
    "advertencia": "warning",
    "error": "error"
}

def translate(code):
    for spanish, english in keywords.items():
        code = code.replace(spanish, english)

    return code

filename = input("File to translate: ")

with open(filename, "r", encoding="utf-8") as file:
    code = file.read()
translated = translate(code)
output = filename.replace(".sc", ".c")

with open(output, "w", encoding="utf-8") as file:
    file.write(translated)

print("Created:", output)