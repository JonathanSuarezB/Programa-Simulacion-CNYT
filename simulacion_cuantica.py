import numpy as np
import matplotlib.pyplot as plt

def deterministic_system(matrix,state,clicks):
    "Funcion para determinar un sistema dada una matriz Booleana, estado inicial y clicks transcurridos"
    new_state = state
    array = []
    for i in range (0,clicks):
        new_state = np.dot(matrix,new_state)
    return np.array(new_state).tolist()

def probabilistic_system(matrix,state,clicks):
    "Funcion para determinar la probabilidad dado un numero de rendijas, objetivos, un estado inicial y clicks transcurridos "
    new_state = state
    m1 = matrix
    for i in range(0, clicks):
        matrix = np.matmul(m1,m1)
    new_state = np.dot(matrix, state)
    return "Matriz:",np.array(matrix).tolist(),"Estado nuevo:",np.array(new_state).tolist()

def quantum_system(matrix,state,clicks):
    "Funcion para determinar la probabilidad dado un numero de rendijas, objetivos, un estado inicial y clicks transcurridos "
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = norma(matrix[i][j])
    new_state = state
    m1 = matrix
    for i in range(0, clicks):
        matrix = np.matmul(m1,m1)
    new_state = np.dot(matrix, state)
    for i in range(len(matrix)):
        if new_state[i] > 1:
            new_state[i] = 0
        for j in range(len(matrix)):
            if matrix[i][j] > 1:
                matrix[i][j] = 0
    return "Matriz:",np.array(matrix).tolist(),"Estado nuevo:",np.array(new_state).tolist()

def grafica(vectores, probabilidades):
    "Funcion para mostrar las probabilidades de un vector de estados "
    data = {}
    for i in range(len(vectores)):
        data[vectores[i]] = probabilidades[i]
    vector = list(data.keys())
    probabilidades = list(data.values())
    fig = plt.figure(figsize=(10, 5))
    plt.bar(vector, probabilidades, color='maroon',
            width=0.4)
    plt.xlabel("Vectores")
    plt.ylabel("Probabilidades")
    plt.title("Probabilidades de un vector de estados")
    plt.show()

def norma(a):
    "Funcion para calcular la norma de un numero complejo"
    norma = (a.real)**2 + (a.imag)**2
    return norma

