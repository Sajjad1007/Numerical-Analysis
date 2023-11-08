# This method can not solve a system of linear equations if any of the diagonal element becomes 0

def forward_elimination(A, b, n):
    det = 1
    
    for k in range(n - 1):
        for i in range((k + 1), n):
            if A[k][k] == 0:
                return False, 0
                
            c = A[i][k] / A[k][k]
            b[i] = b[i] - c * b[k]
            
            for j in range(k, n):
                A[i][j] = A[i][j] - c * A[k][j]
                
        det = det * A[k][k]
    
    det = det * A[k + 1][k + 1]
    return True, det
    

def back_substitution(A, b, n):
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

        
def print_equations(A, b, n):
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
    
flag, det = forward_elimination(A, b, n)
print("The augmented matrix after forward elimination :\n")
print_equations(A, b, n)

if flag == True:
    x = back_substitution(A, b, n)
    print("The roots =", end = " ")
    print(x)
    print("Det(A) = %0.5f" %det)
else:
    print("Error : division by zero occured, roots can not be determined")
    
    
"""
The augmented matrix after forward elimination :

25.00000  5.00000  1.00000  |  106.80000

0.00000  -4.80000  -1.56000  |  -96.20800

0.00000  0.00000  0.70000  |  0.76000

The roots = [0.29048, 19.69048, 1.08571]
Det(A) = -84.00000
"""