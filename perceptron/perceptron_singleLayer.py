# Modelo Perceptron com uma camada

entradas = [[0, 0], [0, 1], [1, 0], [1, 1]]
# Gabarito porta OR (Problema linear)
gabarito = [0, 1, 1, 1]

# Gabarito porta AND (Problema linear)
#gabarito = [0, 0, 0, 1]

peso1 = 0
peso2 = 0
pontos1 = []
pontos2 = []
taxaAprendizagem = 0.1 #Definida manualmente
limiar = (0 + 1)/2 #Definição de limiar com base nas entradas possíveis

while True:
    n = 0
    acerto = 0
    for input in entradas:
        x1 = input[0]
        x2 = input[1]
        output = x1 * peso1 + x2 * peso2

        if output >= limiar:
            output = 1
        else:
            output = 0

        erro = gabarito[n] - output

        if erro != 0:
            peso1 = peso1 + (taxaAprendizagem * x1 * erro)
            peso2 = peso2 + (taxaAprendizagem * x2 * erro)
        else:
            acerto += 1
        n += 1
    eficiencia = (acerto / len(entradas)) * 100
    if eficiencia < 100:
        print(f"A eficiência do Perceptron está em: {eficiencia}%")
        print(f"Pesos: {peso1, peso2}")
        print("__________________________________________________")
    else:
        print(f"A eficiência do Perceptron está em: {eficiencia}%")
        print(f"Peso final: {peso1, peso2}")
        print("__________________________________________________")
        break