#b가 없으면 x1 = 0, x2 = 0인 상태에서 학습시킬 수 없다
#2층 네트워크, L1 : 2, L2 : 1
import numpy as np


X = np.array([[0,0,1,1],[0,1,0,1]]) #2,4
Y = np.array([0, 0, 0, 1]).reshape((1,4))#1,4
W = np.random.rand(1,2) * 2 - 1            #1,2
theta = 0.25
b = 0

def propagate(W, X, b):
    return np.dot(W, X) + b

def sigmoid(X):
    return 1/(1 + np.exp(-X))

def optimizer(W, X, Y, theta, b, H):
    W = W - theta * (1 / Y.shape[1]) * np.dot((H - Y) * H * (1 - H), X.T)
    b = b - theta * np.sum((1 / Y.shape[1]) * (H - Y) * H * (1 - H), axis=1)
    return W, b

def predict(W, X, b):
    H = np.dot(W, X) + b
    H = sigmoid(H)
    H = np.where(H > 0.5, 1, 0)
    return H

for _ in range(1, 301):
    H = propagate(W, X, b)
    H = sigmoid(H)
    W, b = optimizer(W, X, Y, theta, b, H)
    if _ % 10 == 0:
        print('진행: ', _, '현재 W*X+b: ', H)

result = predict(W, X, b)
print(result)



