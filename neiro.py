
from sqlite import save_metrics, get_normalized_metrics
import numpy as np

#1.ЗАПИСЬ ДАННЫХ
save_metrics() # Функция обращается к proc собирает данные и записывает в базу
data = get_normalized_metrics() # Функция вытаскивает уже собранные данные из базы и так как числа большие нормализует их
load = data['load']
print("Загрузка" + str(load))
mem = data['mem']
print("Свободная память" + str(mem))


#3.НЕЙРОСЕТЬ

weights = [0.1,0.1]
alpha = 0.001


def neural_network(input, weight):
    prediction = w_sum(input, weight)
    return prediction

def w_sum(a,b):
    assert(len(a) == len(b))
    output = 0
    for i in range(len(a)):
        output += (a[i] * b[i])
    return output


for iteration in range(4):
    for i in range(len(load)): # проходим по всем образцам
        input = [load[i], mem[i]]
        load_max = [0, 1, 2]
        load_max_al = load_max[1]
        pred = neural_network(input, weights)
        error = (pred - load_max_al) ** 2
        delta = pred - load_max_al
        weights_delta = [input[i] * delta for i in range(len(input))]
        print(f"Prediction: {pred}")
        print(f"Error: {error}")
        print(f"Delta: {delta}")
        print(f"Weights delta: {weights_delta}")
        for i in range(len(weights)):
            weights[i] -= weights_delta[i] * alpha


    print(f"Updated weights: {weights}")