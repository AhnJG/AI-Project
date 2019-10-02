import random
import numpy as np

class Perceptron:
    def __init__(self, eta=0.05, threshold=0):
        self.eta = eta #Learning Rate
        self.threshold = threshold #경계값
        self.W = []
        self.x0 = -1 # 왜 -1이냐? -> 0이 아니면 상관없다
        self.initw()

    #w0, w1, w2 랜덤값 초기화
    def initw(self):
        W = np.random.rand(2,3)
        print(W[0][0])
        print(W[0][1])
        print(W[0][2])
        print(W)

    #def fit(self, ):
    # def fit(self, X, y, epochs=100):
    #     for _ in range(epochs):
    #         for i in range(len(X)):
    #             tx = X[i]
    #             net = 0.0
    #             for j in range(len(self.w)):
    #                 if 0 == j:
    #                     net = self.x0 * self.w[0]
    #                 else:
    #                     net = net + tx[j-1] * self.w[j]
    #
    #             ty = self.fnet(net)
    #             if ty != y[i]:
    #                 self.updatew(tx, y[i]-ty)

    def updatew(self, x, delta):
        for i in range(len(self.w1)):
            '''x의 값에따라 가중치를 변화시킬때 +, -가 달라진다
            예를들어, X = [-1, 0, 1]일때 결과값이 0이 나와야되는데 1이 나왔다면
            W0은 증가시키고 W1은 그대로 W2는 감소시키면된다'''
            if i == 0:
                self.w1[0] = self.w1[0] + self.eta * self.x0 * delta
            else:
                self.w1[i] = self.w1[i] + self.eta * x[i-1] * delta

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


#nn = Perceptron()


W1 = np.random.rand(2,3)
B1 = np.array([-1, -1, -1, -1])
X = np.array([B1,[0, 0, 1, 1],[0, 1, 0, 1]])
Y = np.array([0, 1, 1, 0])
NAND = np.array([1, 1, 1, 0])
OR = np.array([0, 1, 1, 1])

L1 = np.dot(W1, X)
L1 = np.where(L1>=0, 1, 0)

W2 = np.random.rand(1,3)
B2 = np.array([-1, -1, -1, -1])
L1 = np.vstack((B2, L1))

L2 = np.dot(W2, L1)
L2 = np.where(L2>=0, 1, 0)

print(L2)

print(np.log(0))
#Back_Propagate
W2 = W2 + np.sum(0.05 * L1 * (L2 - Y), axis=1)
#nn.fit()



