def swapList(k):
    max = abs(A[k][k])
    
    for i in range((k + 1), n):
        if max < abs(A[i][k]):
            max = A[i][k]
            maxIndx = i
    
    A[k], A[i] = A[i], A[k]
    b[k], b[i] = b[i], b[k]
    return


def forwardElimination(A, b, n):
    det = 1
    
    for k in range(n - 1):
        swapList(k)
        
        for i in range((k + 1), n):    
            c = A[i][k] / A[k][k]
            b[i] = b[i] - c * b[k]
            
            for j in range(k, n):
                A[i][j] = A[i][j] - c * A[k][j]
                
        det = det * A[k][k]
        
    det = det * A[k + 1][k + 1]
    return det
                
    
def backSubstitution(A, b, n):
    x = []
    x.append(b[n - 1] / A[n - 1][n - 1])
    
    for i in range((n - 2), -1, -1):
        sum = 0
        
        for j in range((i + 1), n):
            sum += A[i][j] * x[(n - 1) - j]
            
        b[i] = (b[i] - sum) / A[i][i]
        x.append(b[i])
    
    x.reverse()
    x = [round(elem, 5) for elem in x]
    return x

        
def printEquations(A, b, n):
    for i in range(n):
        for j in range(n):
            print("%.5f" %A[i][j], end = "  ")
        print("|  %.5f" %b[i])
        print()
    
    return
    

# Main code starts from here

A = [[25, 5, 1],
     [64, 8, 1],
     [144, 12, 1]]
b = [106.8, 177.2, 279.2]
n = 3
    
det = forwardElimination(A, b, n)
print("The augmented matrix after forward elimination :\n")
printEquations(A, b, n)

x = backSubstitution(A, b, n)
print("The roots =", end = " ")
print(x)
print("Determinant = %0.5f" %det)