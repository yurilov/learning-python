celsius = int(input())


def convertor(c):
    f = 9 / 5 * c + 32
    return f


fahrenheit = convertor(celsius)
print(fahrenheit)
