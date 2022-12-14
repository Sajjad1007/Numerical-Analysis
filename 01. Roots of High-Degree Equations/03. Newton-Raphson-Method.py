def f(x):
    y = x**2 - 4*x - 5
    return y


def df(x):
    y = 2*x - 4
    return y


def newton_raphson(x):
    n = int(input("Maximum iterations : "))
    
    for i in range(n):
        y = f(x)
        dy = df(x)
        xnew = x - (y / dy)
        
        if abs(xnew - x) < 0.000001:
            print("\nThe root = %0.5f" %xnew, "(%d iterations)" %(i + 1))
            return
        else:
            x = xnew
        
    print("\nThe root = %0.5f" %xnew, "(%d iterations)" %(i + 1))
    return
    

# Main code starts from here

print("The given equation, x^2 - 4x - 5 = 0\n")

x = float(input("Enter initial guess = "))
newton_raphson(x)


"""
The given equation, x^2 - 4x - 5 = 0

Enter initial guess = 7
Maximum iterations : 10

The root = 5.00000 (5 iterations)
"""