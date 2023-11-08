# Quadratic interpolation of Lagrange method

def L_function(t, T):
    sum = ((t - T[1]) / (T[0] - T[1])) * ((t - T[2]) / (T[0] - T[2]))
    return sum


def lagrange(t):
    L = []
    L.append(L_function(t, [T[0], T[1], T[2]]))
    L.append(L_function(t, [T[1], T[2], T[0]]))
    L.append(L_function(t, [T[2], T[0], T[1]]))
    
    sum = 0
    
    for i in range(3):
        sum += (L[i] * V[i])
    
    print("\nv(%g) =" %t, "%g" %sum)
    return

    
# Main code starts from here

T = [10, 15, 20]
V = [227.04, 362.78, 517.35]

t = float(input("Enter t = "))
lagrange(t)


"""
Enter t = 16

v(16) = 392.188
"""