import math

def f(x):
    y = 2000 * math.log(140000 / (140000 - 2100 * x), math.e) - (9.8 * x)
    return y

def trapezoidalMultipleSegment(n):
    a = 8
    b = 30
    h = (b - a) / n
    sum = (f(a) + f(b))
    
    for i in range(1, n):
        sum += (2 * f(a + i * h))
        
    sum *= (h / 2)
    return sum

n = int(input("Number of segments : "))
trueValue = 11061.33554
approximateValue = trapezoidalMultipleSegment(n)
error = 100 * abs((trueValue - approximateValue) / trueValue)
print("\nTrue value =", trueValue)
print("Approximate value =", approximateValue)
print("Error = %f%%" %error)