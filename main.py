import traductor

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


t = Input("Enviar o Recibir (E/R)", ("E", "R"))

if t == 'E':
    m = input("Mensaje: ")
    pair_of_angles = traductor.send(m)
    for pair in pair_of_angles:
        print(pair[0], end=",")
        print(pair[1], end="\t")
    print()
else:
    n = int(input_number("Número de ángulos"))
    pairs = []
    pair = []
    for ni in range(n):
        angle = float(input_number("Introduzca siguiente ángulo"))
        pair.append(angle)
        if ni % 2 == 1:
            pairs.append(tuple(pair))
            pair = []
    print(traductor.receive(pairs))            
