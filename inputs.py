def Input(message, options):
    result = input("{}: ".format(message)).upper()
    

    while result not in options:
        print("Opción incorrecta")
        result = input("{}: ".format(message)).upper()

    return result

def valida_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def input_number(message):
    result = input("{}: ".format(message)).upper()
    while not valida_number(result):
        print("No es un número")
        result = input("{}: ".format(message)).upper()
    return result

