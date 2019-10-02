#b가 없으면 x1 = 0, x2 = 0인 상태에서 학습시킬 수 없다
#2층 네트워크, L1 : 4, L2 : 1 -> 2층 이지만 각 입력에따른 노드를 두면 학습이 가능하다!
import numpy as np


X = np.array([[0,0,1,1],[0,1,0,1]]) #2,4
Y = np.array([0, 1, 1, 0]).reshape((1,4))#1,4
W = np.random.rand(1,2) * 2 - 1            #1,2
theta = 0.25
b = np.zeros((1,4))

def propagate(W, X, b):
    return np.dot(W, X) + b

def sigmoid(X):
    return 1/(1 + np.exp(-X))

def optimizer(W, X, Y, theta, b, H):
    W = W - theta * (1 / Y.shape[1]) * np.dot((H - Y) * H * (1 - H), X.T)
    b = b - theta *(1 / Y.shape[1]) * (H - Y) * H * (1 - H)
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



