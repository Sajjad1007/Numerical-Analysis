def df(x, y):
    y1 = -2.2067 * (10 ** -12) * (y ** 4 - 81 * (10 ** 8))
    return y1


def ralston(xn, h):
    x = 0
    y = 1200
    y_true = 647.57
    
    while x < xn:
        k1 = df(x, y)
        k2 = df(x + h * 3.0 / 4.0, y + h * k1 * 3.0 / 4.0)
        y_new = y + h * (k1 * 1.0 / 3.0 + k2 * 2.0 / 3.0)
        x += h
        y = y_new
    
    error = 100 * abs((y_true - y) / y_true)
    print("\nf(%d) =" %x, y)
    print("Error = %0.5f%%" %error)
    return


# Main code starts from here
    
xn = int(input("Enter x = "))
h = float(input("Enter step size = "))
ralston(xn, h)


"""
Enter x = 480
Enter step size = 240

f(480) = 690.0130899617197
Error = 6.55421%
"""