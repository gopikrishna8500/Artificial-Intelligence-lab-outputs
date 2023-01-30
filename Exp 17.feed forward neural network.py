import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_derivative(x):
    return x * (1 - x)
X = np.array([[1,0,1], [0,1,1], [1,1,1], [0,0,1]])
y = np.array([[1, 1, 0, 0]]).T
num_iterations = 10000
learning_rate = 0.1
input_nodes = 3
output_nodes = 1
weights1 = 2 * np.random.random((input_nodes, 4)) - 1
weights2 = 2 * np.random.random((4, output_nodes)) - 1
for i in range(num_iterations):
    layer1 = sigmoid(np.dot(X, weights1))
    layer2 = sigmoid(np.dot(layer1, weights2))
    layer2_error = y - layer2
    layer2_delta = layer2_error * sigmoid_derivative(layer2)
    layer1_error = layer2_delta.dot(weights2.T)
    layer1_delta = layer1_error * sigmoid_derivative(layer1)
    weights2 += layer1.T.dot(layer2_delta) * learning_rate
    weights1 += X.T.dot(layer1_delta) * learning_rate
print(layer2)
