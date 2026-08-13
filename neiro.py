from sqlite import save_metrics, load_metrics_db

raw_load = load_metrics_db("SELECT load FROM metrics")
raw_mem = load_metrics_db("SELECT mem FROM metrics")
load_metric = [item[0] for item in raw_load]
mem_metrics = [item[0] for item in raw_mem]

# Сохраняем новые метрики
save_metrics()
weights = [0.1, 0.2]
alpha = 0.1


def neural_network(input, weight):
    prediction = w_sum(input, weight)
    return prediction

def w_sum(a,b):
    assert(len(a) == len(b))
    output = 0
    for i in range(len(a)):
        output += (a[i] * b[i])
    return output


for iteration in range(20):
    input = [load_metric[0], mem_metrics[0]]
    load_max = [1]
    load_max_al = load_max[0]
    pred = neural_network(input, weights)
    error = (pred - load_max_al) ** 2
    delta = pred - load_max_al
    weights_delta = [input[i] * delta for i in range(len(input))]
    #weights_delta = input * delta
    print(f"Prediction: {pred}")
    print(f"Error: {error}")
    print(f"Delta: {delta}")
    print(f"Weights delta: {weights_delta}")
    for i in range(len(weights)):
        weights[i] -= weights_delta[i] * alpha


    print(f"Updated weights: {weights}")