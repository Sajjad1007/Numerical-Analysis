from scipy.optimize import newton, bisect, fsolve, root

f = lambda x: x**2 - 4*x - 5
print("Here are some built-in functions for finding numerical solutions\n")

print("newton(f, 0) : root = %0.5f" %newton(f, 0))
print("newton(f, 3) : root = %0.5f" %newton(f, 3))

print("\nbisect(f, 4, 7) : root = %0.5f" %bisect(f, 4, 7))
print("bisect(f, -3, 2) : root = %0.5f" %bisect(f, -3, 2))

print("\nfsolve(f, 0) : root = %0.5f" %fsolve(f, 0))
print("fsolve(f, 3) : root = %0.5f" %fsolve(f, 3))

print("\nroot(f, 0) :", root(f, 0).x)
print("root(f, 3) :")
print(root(f, 3))