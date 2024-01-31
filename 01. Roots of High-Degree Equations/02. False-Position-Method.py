def f(x):
    y = x**2 - 4*x - 5
    return y


def falsePosition(xl, xu):
    yl = f(xl)
    yu = f(xu)
    n = int(input("Maximum iterations : "))

    if yl*yu > 0:
        print("\nRoot can not be determined from %0.5f" %xl, "and %0.5f" %xu)
        return
    else:
        for i in range(n):
            xm = (xu*yl - xl*yu)/(yl-yu)
            ym = f(xm)
            
            if abs(yl*ym) < 0.000001:   # yl*ym == 0
                print("\nThe root = %0.5f" %xm, "(%d iterations)" %(i+1))
                return
            elif yl*ym < 0:        # yl and ym are of opposite sign
                xu = xm
            elif yl*ym > 0:        # yl and ym are of same sign
                xl = xm
        
        print("\nThe root = %0.5f" %xm, "(%d iterations)" %(i+1))
        return


# Main code starts from here

print("\nThe given equation, x^2 - 4x - 5 = 0\n")

xl = float(input("Enter lower guess = "))
xu = float(input("Enter upper guess = "))
falsePosition(xl, xu)


"""
The given equation, x^2 - 4x - 5 = 0

Enter lower guess = 2
Enter upper guess = 7
Maximum iterations : 10

The root = 5.00264 (10 iterations)
"""