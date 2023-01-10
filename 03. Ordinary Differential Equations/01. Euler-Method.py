from math import exp


def df(x, y):
    y1 = 5*exp(-x) - 3*y
    return y1


def ddf(x, y):
    y2 = - (5*exp(-x)) - 3*df(x, y)
    return y2


def dddf(x, y):
    y3 = 5*exp(-x) - 3*ddf(x, y)
    return y3


def euler(xn, h):
    x = 0
    y = 3
    y_err = 0
    
    while x < xn: 
        y1 = y + h * df(x, y)
        y_err = (ddf(x, y) * (h**2)) / 2 + (dddf(x, y) * (h**3)) / 6
        x += h
        y = y1
    
    err = 100 * abs(y_err / y)
    print("\nf(%d) =" %x, y)
    print("Error = %0.5f%%" %err)


# Main code starts from here
    
xn = int(input("Enter x = "))
h = float(input("Enter step size = "))
euler(xn, h)