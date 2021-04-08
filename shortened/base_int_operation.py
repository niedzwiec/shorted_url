import string


def single_number_to_str(number):
    repr = string.digits + string.ascii_lowercase
    return repr[number]


def number_to_str(number, base):
    if number == 0:
        return [0]
    digits = []
    while number:
        digits.append(int(number % base))
        number //= base
    return "".join(list(map(single_number_to_str, digits[::-1])))

