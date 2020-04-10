import traductor
from inputs import *

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
