import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from timeit import default_timer as timer

def feature_normalize(X):
    mu = np.mean(X, axis=0)
    sigma = np.std(X, axis=0)
    X_norm = (X - mu) / sigma
    return X_norm, mu, sigma

def compute_cost(X, Y, theta):
    m = len(Y)
    predictions = X.dot(theta)
    squared_errors = (predictions - Y) ** 2
    return 1 / (2 * m) * np.sum(squared_errors)

def gradient_descent(X, Y, theta, alpha, num_iters):
    for iter in range(num_iters):
        predictions = np.matmul(X, theta)
        errors = predictions - Y
        delta = np.matmul(np.transpose(X), errors)
        theta = theta - (alpha * delta)
    return theta

def plot_model(weights, mu, sigma, X, Y):
    plt.figure(1)
    x = np.array([])
    y = np.array([])
    minX = int(np.min(X))
    maxX = int(np.max(X))
    for i in range(minX, maxX):
        normalized_input = (i - mu) / sigma
        estimated_output = np.matmul(np.transpose(weights), np.array([1, normalized_input]))
        x = np.append(x, i)
        y = np.append(y, estimated_output)
    plt.plot(X, Y, linestyle='None', marker='o')
    plt.plot(x, y)

def plot_cost_contour(X, Y, weights):
    plt.figure(2)
    theta0_vals = np.linspace(weights[0] - 100, weights[0] + 100, 100)
    theta1_vals = np.linspace(weights[0] - 100, weights[0] + 100, 100)
    J = np.zeros((len(theta0_vals), len(theta1_vals)))
    for i, theta0 in enumerate(theta0_vals):
        for j, theta1 in enumerate(theta1_vals):
            theta = np.array([theta0, theta1])
            J[i, j] = compute_cost(X, Y, theta)
    plt.contour(theta0_vals, theta0_vals, J.T, levels=np.logspace(0, 20, 100), cmap='viridis')
    plt.xlabel('Theta 0')
    plt.ylabel('Theta 1')
    plt.title('Contour Plot of Cost Function')
    plt.colorbar(label='Cost')
    plt.legend()

data = pd.read_csv('/home/mvign/Workspaces/TechLearning/MachineLearning/src/linear_regression/train.csv')
input = np.array(data.iloc[:, :-1].values.reshape(1, -1)[0])
output = np.array(data.iloc[:, -1].values.reshape(1, -1)[0])
total_iters = 100
learning_rate = 0.0001
weights = np.zeros(2)

start = timer()
normalized_input, mu, sigma = feature_normalize(input)
formatted_input = np.c_[np.ones(normalized_input.shape[0]), normalized_input]
weights = gradient_descent(formatted_input, output, weights, learning_rate, total_iters)
print(weights)
print(timer() - start)
plot_model(weights, mu, sigma, input, output)
plot_cost_contour(formatted_input, output, weights)

plt.show()