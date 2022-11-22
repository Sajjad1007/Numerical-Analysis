from math import sqrt

print("The given equation, 2x^2 - 5x + 3 = 0")
print("Analytical solutions are : x = 1, 1.5\n")

x1 = float(input("Enter initial guess for x1 : "))
x2 = float(input("Enter initial guess for x2 : "))
print()

for i in range(100):
    xnew = (2 * x1**2 + 3) / 5
    
    if abs(xnew - x1) <= 0.000001:
        x1 = xnew
        break
    else:
        x1 = xnew

for j in range(100):
    xnew =  sqrt((5 * x2 - 3) / 2)
    
    if abs(xnew - x2) <= 0.000001:
        x2 = xnew
        break
    else:
        x2 = xnew
        
print("x1 = %0.5f" %x1)
print("Number of iterations :", i+1)
        
print("\nx2 = %0.5f" %x2)
print("Number of iterations :", j+1)