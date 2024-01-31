import math


def f(x):
    y = 2000*math.log(140000/(140000-2100*x), math.e) - 9.8*x
    return y


def trapezoidal(n):
    a = 8
    b = 30
    h = (b-a)/n
    I = f(a)+f(b)
    
    for i in range(1, n):
        a += h
        I += (2*f(a))
        
    I *= (h/2)
    I_true = 11061.33554
    error = 100*abs((I_true-I)/I_true)
    
    print("\nTrue value =", I_true)
    print("Approximate value =", I)
    print("Error = %f%%" %error)
    return


# Main code starts from here

n = int(input("\nNumber of segments : "))
trapezoidal(n)


"""
Number of segments : 10

True value = 11061.33554
Approximate value = 11069.583542061686
Error = 0.074566%
"""