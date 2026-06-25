import numpy as np

def sigmoid(x): return 1 / (1 + np.exp(-x))
def sigmoid_d(x): return x * (1 - x)

#XOr problem - a simple neural net test

x = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

np.random.seed(42)
w1 = np.random.randn(2,4) * 0.5 #input hidden weight
w2 = np.random.randn(4,1) * 0.5 #hidden- output weight

lr = 0.5 #learning rate
losses = []

for epoch in range(10000):
    #forward pass
    h= sigmoid(x @ w1)
    o = sigmoid(h @ w2)

    #loss (Mean squared Error)
    loss = np.mean((y - o)**2)

    losses.append(loss)

    #backend pass - compute graduents
    d_o = (o - y) * sigmoid_d(o)
    d_h  = (d_o @ w2.T) * sigmoid_d(h)

    #update weights

    w2 -= lr * h.T @ d_o
    w1 -= lr * x.T @ d_h

import matplotlib.pyplot as plt
plt.plot(losses); plt.title('loss Decreasig during Traning')
plt.xlabel('Epochs'); plt.ylabel('loss'); plt.show()

print('final predictions (should be close to [0,1,1,0]):')
print(np.round(o,2))