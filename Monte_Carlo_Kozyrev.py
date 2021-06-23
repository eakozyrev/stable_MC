import numpy as np
import matplotlib.pyplot as plt
import math
import array as array

def gen_stable(price):

    data = []
    Prices = []
    Returns10 = []
    Prices.append(price)
    newprice = price
    for i in range(750):
        U = np.pi*np.random.random_sample() - np.pi/2.
        W = np.random.exponential(1)
        X = math.sin(1.7*U)/(math.cos(U))**(1./1.7)*(math.cos(U-1.7*U)/W)**(-0.7/1.7)
        Y = X + 1
        data.append(Y)
        newprice = (1+Y)*newprice
        Prices.append(newprice)
    i = 0
    while i < len(Prices)-10:
        Returns10.append((Prices[i+10] - Prices[i])/Prices[i])
        i = i + 1
    Returns10.sort()
    quantile = Returns10[int(len(Prices)/100.+1)]
    return quantile

def test(data1, data2):
    i = 1
    n1 = 0
    n2 = 0
    data1.sort()
    data2.sort()
    bprint = True
    freq = []
    btv = data1[0] > data2[0]
    chet = 1
    while i < len(data1):
        if btv == (data1[i] > data2[i]):
            chet += 1
        else:
            freq.append(chet)
            chet = 1
            btv = (data1[i] > data2[i])
        if len(freq) > 10 and max(freq) < 0.5*i and bprint == True:
            print('minimal number of MC events = ' + str(i))
            bprint = False
        i+=1
    plt.figure(2)
    plt.hist(freq,100)

    
if __name__ == "__main__":

    data0001 = []
    data1000 = []
    for i in range(4000):
        data0001.append(gen_stable(0.0001))
        data1000.append(gen_stable(1000))
    plt.figure(1)    
    plt.hist(data0001 + data1000,100)
    plt.xlabel('0.01 quantile of 10-days overlapping returns')
    test(data0001,data1000)
    plt.show()
