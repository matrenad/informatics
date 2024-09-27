x = input().split(" ")
y = input().split(" ")
def MNK(x, y):
    import numpy as np
    x = np.array(list(map(float, x)))
    y = np.array(list(map(float, y)))
    a = round(((x*y).mean() - (x.mean()*y.mean())) /((x*x).mean() - (x.mean()*x.mean())),3)
    b = round(y.mean() - a * x.mean(), 3)
    return a, b
print(MNK(x,y))
