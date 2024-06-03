# Modelo de Peceptron com duas camadas
import random
import math

entradas = [[0, 0], [0, 1], [1, 0], [1, 1]]
# Gabarito porta XOR (Problema não linear)
gabarito = [1, 0, 0, 1]

# Gabarito porta AND
#gabarito = [0, 0, 0, 1]
tentativas = 1
peso1 = random.random()
peso1_1 = random.random()
peso1_2 = random.random()
peso2 = random.random()
peso2_1 = random.random()
peso2_2 = random.random()
pesoOut = random.random()
pesoOut2 = random.random()
pesoOut3 = random.random()
taxaAprendizagem = 0.1 #Definida manualmente
limiar = 0.5 #Definição de limiar com base nas entradas possíveis

def sigmoide(x):
    sigmoid = 1/(1+math.exp(-x))
    return sigmoid

def sigmoid_derivada(x):
    return x * (1 - x)

while True:
    n = 0
    acerto = 0
    for input in entradas:
        x1 = input[0]
        x2 = input[1]
        output = sigmoide(x1 * peso1 + x2 * peso2)
        output2 = sigmoide(x1 * peso1_1 + x2 * peso2_1)
        output3 = sigmoide(x1 * peso1_2 + x2 * peso2_2)

        saida = output * pesoOut + output2 * pesoOut2 + output3 * pesoOut3

        if saida >= limiar:
            saida = 1
        else:
            saida = 0

        erro = gabarito[n] - saida

        if erro != 0:
            pesoOut = pesoOut + (taxaAprendizagem * output * erro)
            pesoOut2 = pesoOut2 + (taxaAprendizagem * output2 * erro)
            pesoOut3 = pesoOut3 + (taxaAprendizagem * output3 * erro)

            delta_output1 = erro * pesoOut * sigmoid_derivada(output)
            delta_output2 = erro * pesoOut2 * sigmoid_derivada(output2)
            delta_output3 = erro * pesoOut3 * sigmoid_derivada(output3)

            peso1 = peso1 + (taxaAprendizagem * x1 * delta_output1)
            peso2 = peso2 + (taxaAprendizagem * x2 * delta_output1)
            peso1_1 = peso1_1 + (taxaAprendizagem * x1 * delta_output2)
            peso2_1 = peso2_1 + (taxaAprendizagem * x2 * delta_output2)
            peso1_2 = peso1_2 + (taxaAprendizagem * x1 * delta_output3)
            peso2_2 = peso2_2 + (taxaAprendizagem * x2 * delta_output3)
        else:
            acerto += 1
        n += 1
    eficiencia = (acerto / len(entradas)) * 100
    if eficiencia < 100:
        print(f"A eficiência do Perceptron está em: {eficiencia}%")
        print(f"Peso1: {peso1}, Peso2: {peso2}\n Peso1-1: {peso1_1}, Peso2_1:"
              f" {peso2_1}\n Peso1_2: {peso1_2}, Peso1_2: {peso2_1}\n PesoOut: "
              f"{pesoOut}, PesoOut2: {pesoOut2}, PesoOut: {pesoOut3}")
        print(f"Tentativas: {tentativas}")
        print("__________________________________________________")
    else:
        print(f"A eficiência do Perceptron está em: {eficiencia}%")
        print(f"Peso1: {peso1}, Peso2: {peso2}\nPeso1-1: {peso1_1}, Peso2_1:"
              f" {peso2_1}\nPeso1_2: {peso1_2}, Peso1_2: {peso2_1}\nPesoOut: "
              f"{pesoOut}, PesoOut2: {pesoOut2}, PesoOut: {pesoOut3}")
        print(f"Tentativas: {tentativas}")
        print("__________________________________________________")
        break
    tentativas += 1