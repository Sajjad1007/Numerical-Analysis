import math


def f(x):
    y = 2000*math.log(140000/(140000-2100*x), math.e) - 9.8*x
    return y


def simpson(n):
    a = 8
    b = 30
    h = (b-a)/n
    I = f(a)+f(b)
    
    for i in range(1, n):
        a += h
        
        if i % 2 == 1:
            I += (4*f(a))
        else:
            I += (2*f(a))
    
    I *= (h/3)
    I_true = 11061.33554
    error = 100*abs((I_true-I)/I_true)
    
    print("\nTrue value =", I_true)
    print("Approximate value =", I)
    print("Error = %f%%" %error)
    return


# Main code starts from here

n = int(input("\nNumber of segments(even) : "))
simpson(n)


"""
Number of segments(even) : 10

True value = 11061.33554
Approximate value = 11061.343468407498
Error = 0.000072%
"""