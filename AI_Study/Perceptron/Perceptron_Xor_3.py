#b가 없으면 x1 = 0, x2 = 0인 상태에서 학습시킬 수 없다
#3층 네트워크, 1L : 2, 2L : 1, 3L : 1
import numpy as np

X = np.array([[0,0,1,1],[0,1,0,1]]) #2,4
Y = np.array([0, 1, 1, 0]).reshape((1,4))#1,4
W1 = np.random.rand(1,2) * 2 - 1    #1,2
W2 = np.random.rand(1,1) * 2 - 1    #1,1
theta = 0.1
b1 = 0
b2 = 0

def propagate(W1, W2, b1, b2, X):
    L1 = sigmoid((np.dot(W1, X) + b1)) #(1,2)*(2,4) -> (1,4)
    L2 = sigmoid(W2 * L1 + b2) #(1,1)*(1,4) -> (1,4)
    return L1, L2

def sigmoid(X):
    return 1/(1 + np.exp(-X))

def optimizer(W1, W2, b1, b2, L1, L2, X, Y, theta):
    W1 = W1 - theta * np.dot((1 / Y.shape[1]) * (L2 - Y) * (L2) * (1 - L2) * W2 * (L1) * (1 - L1), X.T)
    b1 = b1 - theta * np.sum((1 / Y.shape[1]) * (L2 - Y) * (L2) * (1 - L2) * W2 * (L1) * (1 - L1), axis=1)
    W2 = W2 - theta * (1 / Y.shape[1]) * (L2 - Y) * (L2) * (1 - L2) * L1
    b2 = b2 - theta * np.sum((1 / Y.shape[1]) * (L2 - Y) * (L2) * (1 - L2), axis=1)
    return W1, b1, W2, b2

def predict(X):
    _, pre = propagate(W1, W2, b1, b2, X)
    pre = np.where(pre > 0.5, 1, 0)
    return pre

for _ in range(1, 301):
    L1, L2 = propagate(W1, W2, b1, b2, X)
    W1, b1, W2, b2 = optimizer(W1, W2, b1, b2, L1, L2, X, Y, theta)

    if _ % 10 == 0:
        print('진행: ', _, '현재 W*X+b: ', L2)

result = predict(X)
print(result)



