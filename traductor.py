unidad = 22.5

def num_to_angles(value):
    first = value // 16 * unidad
    second = value % 16 * unidad
    return first, second

def pair_angles_to_num(angles):
    return int((angles[0] * 16 + angles[1]) / unidad)


def send(message):
    message = str(message)
    angles = []
    for char in message:
        angles.append(num_to_angles(ord(char)))
    return angles

def receive(angles):
    result = ""
    for pangles in angles:
        char = chr(pair_angles_to_num(pangles))
        result += char

    return result
        