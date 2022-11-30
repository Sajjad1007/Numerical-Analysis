import math

def f(x):
    y = 2000 * math.log(140000 / (140000 - 2100 * x), math.e) - (9.8 * x)
    return y

def simpsonsMultipleSegment(n):
    a = 8
    b = 30
    h = (b - a) / n
    sum = f(a) + f(b)
    
    for i in range(1, n):
        if i % 2 == 1:
            sum += (4 * f(a + i * h))
        else:
            sum += (2 * f(a + i * h))
    
    sum *= (h / 3)
    return sum

n = int(input("Number of segments(even number) : "))
trueValue = 11061.33554
approximateValue = simpsonsMultipleSegment(n)
error = 100 * abs((trueValue - approximateValue) / trueValue)
print("\nTrue value =", trueValue)
print("Approximate value =", approximateValue)
print("Error = %f%%" %error)