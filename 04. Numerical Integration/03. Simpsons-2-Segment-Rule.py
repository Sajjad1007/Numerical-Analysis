import math


def f(x):
    y = 2000 * math.log(140000 / (140000 - 2100 * x), math.e) - (9.8 * x)
    return y


def simpsons2Segment(n):
    a = 8
    b = 30
    c = (a + b) / 2
    h = (b - a) / n
    I = (f(a) + f(b) + 4 * f(c)) * (h / 3)
    It = 11061.33554
    error = 100 * abs((It - I) / It)
    
    print("True value =", It)
    print("Approximate value =", I)
    print("Error = %f%%" %error)
    return


# Main code starts from here

simpsons2Segment(2)