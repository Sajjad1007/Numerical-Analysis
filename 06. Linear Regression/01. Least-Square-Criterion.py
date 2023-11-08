def least_square(x, y, n):
    sum_xy = sum_x = sum_y = 0
    sum_x_square = 0
    
    for i in range(n):
        sum_xy += x[i] * y[i]
        sum_x += x[i]
        sum_y += y[i]
        sum_x_square += x[i] ** 2
        
    a1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x_square - sum_x ** 2)
    a0 = (sum_y - a1 * sum_x) / n
    print("The linear regression model : y = %fx" %a1, "+ %f" %a0)
    return
    

# Main code starts from here
    
x = [0.698132, 0.959931, 1.134464, 1.570796, 1.919862]
y = [0.188224, 0.209138, 0.230052, 0.250965, 0.313707]
least_square(x, y, 5)


"""
The linear regression model : y = 0.096091x + 0.117665
"""