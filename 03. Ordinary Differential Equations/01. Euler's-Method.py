def df(x, y):
    y1 = -2.2067 * (10 ** -12) * (y ** 4 - 81 * (10 ** 8))
    return y1


def euler(xn, h):
    x = 0
    y = 1200
    y_true = 647.57
    
    while x < xn:
        y_new = y + h * df(x, y)
        x += h
        y = y_new
    
    error = 100 * abs((y_true - y) / y_true)
    print("\nf(%d) =" %x, y)
    print("Error = %0.5f%%" %error)
    return


# Main code starts from here
    
xn = int(input("Enter x = "))
h = float(input("Enter step size = "))
euler(xn, h)


"""
Enter x = 480
Enter step size = 240

f(480) = 110.31739981426284
Error = 82.96441%
"""