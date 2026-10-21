from math import exp


def softmax(valori):
    if not valori:
        return []

    exponentiale = [exp(x) for x in valori]
    suma = sum(exponentiale)
    return [valoare / suma for valoare in exponentiale]

a = [-0.4, 0, 0.2, 0.2, 0.4]
print(softmax(a))
