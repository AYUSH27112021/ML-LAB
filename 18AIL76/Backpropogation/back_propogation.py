import numpy as np
x = np.array(([2,9],[1,5], [3,6]), dtype=float)
y = np.array(([92],[86],[89]), dtype=float)
X = x/np.amax(x, axis=0)
Y = y/100
def sigmoid(x):
    return (1/(1+np.exp(-x)))
def der_sigmoid(x):
    return x*(1-x)
epoch = 90000 # Do for even 5K and 9K
lr = 0.1 # Do for 0.2 also
ip = 2
hidden = 3
op = 1
wh = np.random.uniform(size=(ip,hidden))
bh = np.random.uniform(size=(1,hidden))
wo = np.random.uniform(size=(hidden,op))
bo = np.random.uniform(size=(1,op))
for i in range(epoch):
    hinp1 = np.dot(X,wh)
    hinp = hinp1+bh
    hlayer = sigmoid(hinp)
    oinp1 = np.dot(hlayer,wo)
    oinp = oinp1+bo
    olayer = sigmoid(oinp)
    EO = y - olayer
    outgrad = der_sigmoid(olayer)
    dout = EO*outgrad
    EH = dout.dot(wo.T)
    hiddengrad = der_sigmoid(hlayer)
    dhid = EH*hiddengrad
    wo += hlayer.T.dot(dout)*lr
    wh += X.T.dot(dhid)*lr
print('Input\n',str(X))
print('Actual Output\n', str(y))
print('Predicted Output\n', olayer)