import math

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
    n = 3 # συντελεστές πολυωνύμου
    A = [[None for j in range(n)] for i in range(len(x))]
    for i in range(len(x)):
        for j in range(n):
            A[i][j] = math.pow(x[i], j)
    P, L, U = PLU(multiMatrix(AT(A), A))
    s = solverU(U, solverL(L, multi(P, multi(AT(A), y))))
    return s


ΑΡΑΙΓ = [95000, 93900, 92400, 94900, 93600, 92000, 91800, 92400, 92300, 92500] # Aegean Airlines
ΕΛΠΕ = [80600, 79000, 79200, 80300, 80500, 77500, 78200, 77800, 77700, 76000] # Hellenic Petroleum
DATE = [8, 9, 10, 11, 14, 15, 16, 17, 18, 21]
print(Square(DATE, ΕΛΠΕ))
