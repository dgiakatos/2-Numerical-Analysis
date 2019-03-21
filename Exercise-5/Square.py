import math
import random

def AT(A):
    B = [[None for j in range(len(A))] for i in range(len(A[0]))]
    for i in range(len(A[0])):
        for j in range(len(A)):
            B[i][j] = A[j][i]
    return B


def multiMatrix(A, B):
    AB = [[0 for j in range(len(B[0]))] for i in range(len(A))]
    if len(A[0]) != len(B):
        exit(1)

    for k in range(len(A)):
        for i in range(len(B[0])):
            for j in range(len(B)):
                AB[i][k] = AB[i][k] + A[i][j] * B[j][k]
    return AB


def multi(A, b):
    Ab = [0 for i in range(len(A))]
    if len(A[0]) != len(b):
        exit(1)
    for i in range(len(A)):
        for j in range(len(A[0])):
            Ab[i] = Ab[i] + A[i][j] * b[j]
    return Ab


def PLU(A):
    P = [[0 for j in range(len(A))] for i in range(len(A))]
    L = [[0 for j in range(len(A))] for i in range(len(A))]
    for i in range(len(A)):
        P[i][i] = 1
    for i in range(0, len(A)):
        maxElement = math.fabs(A[i][i])
        maxRow = i
        for j in range(i+1, len(A)):
            if math.fabs(A[j][i]) > maxElement:
                maxElement = math.fabs(A[j][i])
                maxRow = j
        for j in range(0, len(A)):
            temp = A[maxRow][j]
            A[maxRow][j] = A[i][j]
            A[i][j] = temp
            tempP = P[maxRow][j]
            P[maxRow][j] = P[i][j]
            P[i][j] = tempP
            tempL = L[maxRow][j]
            L[maxRow][j] = L[i][j]
            L[i][j] = tempL
        for j in range(i + 1, len(A)):
            g = A[j][i] / A[i][i]
            L[j][i] = g
            for k in range(i, len(A)):
                if i == k:
                    A[j][k] = 0
                else:
                    A[j][k] = - g * A[i][k] + A[j][k]
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                L[j][i] = 1
    U = A
    return P, L, U


def solverU(A, b):
    x = []
    for i in range(len(A)):
        x.append(None)
    for i in range(len(A) - 1, -1, -1):
        k = len(A) - 1
        temp = 0
        for j in range(len(A[0]) - 1, -1, -1):
            if x[k] is None:
                break
            temp = temp + A[i][j] * x[k]
            k = k - 1
        x[i] = (b[i] - temp) / A[i][i]
    return x


def solverL(A, b):
    x = []
    for i in range(len(A)):
        x.append(None)
    for i in range(len(A)):
        k = 0
        temp = 0
        for j in range(len(A[0])):
            if x[k] is None:
                break
            temp = temp + A[i][j] * x[k]
            k = k + 1
        x[i] = b[i] - temp
    return x


def Square(x, y):
    n = 4 # συντελεστές πολυωνύμου
    A = [[None for j in range(n)] for i in range(len(x))]
    for i in range(len(x)):
        for j in range(n):
            A[i][j] = math.pow(x[i], j)
    P, L, U = PLU(multiMatrix(AT(A), A))
    s = solverU(U, solverL(L, multi(P, multi(AT(A), y))))
    return s


a = [3.896993427370104, 4.523972077193033, 3.0057603845271466, 5.306644151423592, 2.4114357407564224, -0.7850479654803975, 6.224182513472877, -2.9030655628024267, -2.620853477468518, -4.473053298914355]
b = [-0.6855804857536925, -0.9823019863592075, 0.13541496082078464, -0.8285657522382525, 0.6669865542203343, -0.7068591105104192, -0.05896856496931816, -0.23627167644939231, -0.49752147325751334, 0.9714956707647036]
print(Square(a, b))
