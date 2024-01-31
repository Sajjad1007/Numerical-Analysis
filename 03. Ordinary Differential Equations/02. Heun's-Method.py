def df(x, y):
    y1 = -2.2067*(10**-12)*(y**4 - 81*(10**8))
    return y1


def heun(xn, h):
    x = 0
    y = 1200
    y_true = 647.57
    
    while x < xn:
        k1 = df(x, y)
        k2 = df(x+h, y+k1*h)
        y_new = y + h*0.5*(k1+k2)
        x += h
        y = y_new
    
    error = 100*abs((y_true-y)/y_true)
    print("\nf(%d) =" %x, y)
    print("Error = %0.5f%%" %error)
    return


# Main code starts from here
    
xn = int(input("\nEnter x = "))
h = float(input("Enter step size = "))
heun(xn, h)


"""
Enter x = 480
Enter step size = 240

f(480) = 584.2684867703111
Error = 9.77524%
"""