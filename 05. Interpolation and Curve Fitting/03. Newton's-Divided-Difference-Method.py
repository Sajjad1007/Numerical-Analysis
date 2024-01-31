# Quadratic interpolation of Newton's Divided Difference method

def newton(t):
    B = []
    
    b0 = V[0]
    B.append(b0)
    
    b1 = ((V[1]-V[0])/(T[1]-T[0]))
    B.append(b1)
    
    b2 = (((V[2]-V[1])/(T[2]-T[1]))-b1)/(T[2]-T[0])
    B.append(b2)
    
    sum = B[0] + B[1]*(t-T[0]) + B[2]*(t-T[0])*(t-T[1])
    print("\nv(%g) =" %t, "%g" %sum)
    return

    
# Main code starts from here

T = [10, 15, 20]
V = [227.04, 362.78, 517.35]

t = float(input("\nEnter t = "))
newton(t)


"""
Enter t = 16

v(16) = 392.188
"""