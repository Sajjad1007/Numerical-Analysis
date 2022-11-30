from math import sqrt

def fixedPointIteration(x1, x2):
    n = int(input("Maximum iterations : "))
    
    for i in range(n):
        d = 4*x1 + 5        
        xnew = sqrt(d)

        if abs(xnew - x1) < 0.000001:
            x1 = xnew
            break
        else:
            x1 = xnew

    for j in range(n):
        xnew = (x2**2 - 5) / 4

        if abs(xnew - x2) < 0.000001:
            x2 = xnew
            break
        else:
            x2 = xnew

    print("\nThe roots = %0.5f" %x1, "(%d iterations)," %(i + 1), "%0.5f" %x2, "(%d iterations)" %(j + 1))
    return


print("The given equation, x^2 - 4x - 5 = 0\n")

x1 = float(input("Enter 1st initial guess = "))
x2 = float(input("Enter 2nd initial guess = "))
fixedPointIteration(x1, x2)