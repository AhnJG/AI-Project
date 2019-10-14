import random
import numpy as np

class Perceptron:
    def __init__(self, eta=0.05, threshold=0):
        self.eta = eta #Learning Rate
        self.threshold = threshold #경계값
        self.w = []
        self.x0 = -1 # 왜 -1이냐? -> 0이 아니면 상관없다,
        self.initw()

    #w0, w1, w2 랜덤값 초기화
    def initw(self):
        for _ in range(3):
            self.w.append(random.random())

    def fit(self, X, y, epochs=100):
        for _ in range(epochs):
            for i in range(len(X)):
                tx = X[i]
                net = 0.0
                for j in range(len(self.w)):
                    if 0 == j:
                        net = self.x0 * self.w[0]
                    else:
                        net = net + tx[j-1] * self.w[j]

                ty = self.fnet(net)
                if ty != y[i]:
                    self.updatew(tx, y[i]-ty)

    def updatew(self, x, delta):
        for i in range(len(self.w)):
            '''x의 값에따라 가중치를 변화시킬때 +, -가 달라진다
            예를들어, X = [-1, 0, 1]일때 결과값이 0이 나와야되는데 1이 나왔다면
            W0은 증가시키고 W1은 그대로 W2는 감소시키면된다'''
            if i == 0:
                self.w[0] = self.w[0] + self.eta * self.x0 * delta
            else:
                self.w[i] = self.w[i] + self.eta * x[i-1] * delta

    def fnet(self, net):
        if net >= self.threshold:
            return 1
        else:
            return 0

    def predict(self, X):
        y = []
        for i in range(len(X)):
            tx = X[i]
            net = 0.0
            for j in range(len(self.w)):
                if j == 0:
                    net = net + self.x0 * self.w[0]
                else:
                    net = net + tx[j-1] * self.w[j]
            ty = self.fnet(net)
            y.append(ty)
        return y

    def model_nand(self):
        X = [[0, 0], [0, 1], [1, 0], [1, 1]]
        y = [1, 1, 1, 0]
        self.fit(X, y, 35)
        py = self.predict(X)
        return py

    def model_or(self):
        X = [[0, 0], [0, 1], [1, 0], [1, 1]]
        y = [0, 1, 1, 1]
        self.fit(X, y, 10)
        py = self.predict(X)
        return py

    def model_xor(self):
        X = np.array([self.model_nand(), self.model_or()]).T
        Y = [0, 1, 1, 0]
        self.fit(X, Y, 10)
        py = self.predict(X)
        return py

nn = Perceptron()
print('OR:',nn.model_or())
print('NAND:',nn.model_nand())
print('XOR:',nn.model_xor())




