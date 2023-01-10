import math


def f(x):
    y = 2000 * math.log(140000 / (140000 - 2100 * x), math.e) - (9.8 * x)
    return y


def simpsonsMultipleSegment(n):
    a = 8
    b = 30
    h = (b - a) / n
    I = f(a) + f(b)
    
    for i in range(1, n):
        if i % 2 == 1:
            I += (4 * f(a + i * h))
        else:
            I += (2 * f(a + i * h))
    
    I *= (h / 3)
    It = 11061.33554
    error = 100 * abs((It - I) / It)
    
    print("\nTrue value =", It)
    print("Approximate value =", I)
    print("Error = %f%%" %error)
    return


# Main code starts from here

n = int(input("Number of segments(even number) : "))
simpsonsMultipleSegment(n)