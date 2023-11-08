def f(x):
    y = x ** 2 - 4 * x - 5
    return y


def secant(x1, x2):
    n = int(input("Maximum iterations : "))
    
    for i in range(n):
        y1 = f(x1)
        y2 = f(x2)
        x_new = x2 - y2 * ((x2 - x1) / (y2 - y1))
        
        if abs(x_new - x2) < 0.000001:
            print("\nThe root = %0.5f" %x_new, "(%d iterations)" %(i + 1))
            return
        else:
            x1 = x2
            x2 = x_new
        
    print("\nThe root = %0.5f" %x_new, "(%d iterations)" %(i + 1))
    return
    

# Main code starts from here

print("The given equation, x^2 - 4x - 5 = 0\n")

x1 = float(input("Enter 1st initial guess = "))
x2 = float(input("Enter 2nd initial guess = "))
secant(x1, x2)


"""
The given equation, x^2 - 4x - 5 = 0

Enter 1st initial guess = 2
Enter 2nd initial guess = 7
Maximum iterations : 10

The root = 5.00000 (7 iterations)
"""