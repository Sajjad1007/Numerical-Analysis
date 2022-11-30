import math

def f(x):
    y = 2000 * math.log(140000 / (140000 - 2100 * x), math.e) - (9.8 * x)
    return y

def trapezoidalSingleSegment(n):
    a = 8
    b = 30
    h = (b - a) / n
    sum = (f(a) + f(b)) * (h / 2)
    return sum

trueValue = 11061.33554
approximateValue = trapezoidalSingleSegment(1)
error = 100 * abs((trueValue - approximateValue) / trueValue)
print("True value =", trueValue)
print("Approximate value =", approximateValue)
print("Error = %f%%" %error)