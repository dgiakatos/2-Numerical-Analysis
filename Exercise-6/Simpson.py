import random
import math


def Sort(a):
    for i in range(len(a)):
        for j in range(1, len(a)-i):
            if a[j-1] > a[j]:
                temp = a[j-1]
                a[j-1] = a[j]
                a[j] = temp
    return a


def Simpson(x):
    xi = []
    f = []
    for i in range(len(x)):
        xi.append(x[0] + i * (x[len(x)-1] - x[0]) / (len(x) - 1))
        f.append(math.sin(xi[i]))
    sum1 = 0
    for i in range(1, int(len(x)/2 - 1)):
        sum1 = sum1 + f[2*i]
    sum2 = 0
    for i in range(1, int(len(x)/2)):
        sum2 = sum2 + f[2*i-1]
    return ((x[len(x)-1] - x[0]) / (3 * (len(x) - 1))) * (f[0] + f[len(x)-1] + 2*sum1 + 4*sum2), (math.pow(x[len(x)-1] - x[0], 5) / (180 * math.pow(len(x) - 1, 4))) * 1

'''
a = []
for i in range(10):
    a.append(random.uniform(0.1, math.pi/2))
a[0] = 0
a[9] = math.pi/2
'''
a = [0, 0.7145354001734879, 0.7504025754330428, 0.6292925583709822, 0.7162486150150638, 1.4279559200937, 0.6196131447899629, 0.8962171826862333, 0.38295764376347563, 1.5707963267948966]
print(Simpson(Sort(a)))
