def f(x):
    y = x**2 - 4*x - 5
    return y


def bisection(xl, xh):
    yl = f(xl)
    yh = f(xh)
    n = int(input("Maximum iterations : "))

    if yl * yh > 0:
        print("\nThe root is not within %0.5f" %xl, "and %0.5f" %xh)
        return
    else:
        for i in range(n):
            xm = (xl + xh) / 2
            ym = f(xm)
            
            if abs(ym) < 0.000001:  # if yl * ym == 0
                print("\nThe root = %0.5f" %xm, "(%d iterations)" %(i + 1))
                return
            elif yl * ym < 0:       # if yl and ym are of opposite sign then xh = xm
                xh = xm
            elif yl * ym > 0:       # if yl and ym are of same sign then xl = xm
                xl = xm
        
        print("\nThe root = %0.5f" %xm, "(%d iterations)" %(i + 1))
        return


print("The given equation, x^2 - 4x - 5 = 0\n")

xl = float(input("Enter lower guess = "))
xh = float(input("Enter upper guess = "))
bisection(xl, xh)