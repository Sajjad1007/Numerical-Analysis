#!/usr/bin/env python
# coding: utf-8

# # Python For Data Science
# ### Starting The Journey

# In[89]:


print("Hello""World")
print('Hello','World')


# To run iPython Shell, type `ipython` command in Anaconda Powershell Prompt.  
# iPython Shell works almost like a calculator.

# In[44]:


print("Before single line comment")
#This is single line comment
print("Single comment has not been printed")
print()

print("Before multiple line comments")
"""
This is multiple line comment
I am Sajjadur Rahman
I am learning python language
"""
print("Multiple comments have not been printed")


# ### Variables

# In[89]:


a, b, c, d, e, x = 3, 5.2, 2-4j, "Hello", True, 10
print(type(a+b))
del x                       #x will be deleted


# In[90]:


get_ipython().run_line_magic('whos', '')


# ### Operators

# In[91]:


print(5/2)                  #normal division
print(5//2)                 #floor division
print("Hello" + "Sajjad")   #concatenation
2**4                        #2 to the power 4


# Variable naming rules are same as C/C++/Java.  
# Underscore(_) stores the last value that we did not assign to a particular variable explicity.

# In[92]:


print(_)


# In Python, logical operators are : `and`, `or`, `not`.
# ### Some Useful Functions

# In[93]:


print(round(5.6231))
print(round(4.55852,3))


# In[94]:


print(divmod(27,5))         #prints (quotient, remainder)


# In[95]:


print(isinstance(1,int))
print(isinstance(1.0,int))
print(isinstance(1.0,(int,float)))


# In[98]:


print(pow(2,5))             #2 to the power 5
print(pow(2,5,10))          #(2 to the power 5) mod 10


# input() function accepts inputs from the user as a `str` type data.

# In[99]:


x = input("Enter x = ")
print(type(x))
x = int(x)
print(type(x))


# ### Control Statements

# In[100]:


a = float(input("Enter a = "))
b = float(input("Enter b = "))

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")
    
print("a > b") if a > b else print("a < b") if a < b else print("a = b")
print(int(b))


# ### Loops

# In[14]:


n = int(input("Enter n = "))
i = 1
while i < n:
    if i%2 == 0:
        print(i)
    else:
        pass
    i += 1


# In[78]:


L = []
for i in range(0, 10, 2):   #range(start location, end location, jump), 10 will not be included
    L.append(i)
print(L)
print("Length =", len(L))


# In[17]:


S = {"apple", 4.9, "cherry"}
for x in S:
    print(x)
    #break
else:     #if we forcefully terminate the loop by 'break' statement, 'else' bock will not be executed
    print("Loop terminates completing all of its iterations")
print("Outside the loop")


# ### Functions
# Whenever placing ? and ?? after any function gives us the same output in the window, that means the function is not written in plain python, it is written in some other language and used in python.

# In[51]:


def printName(name):
    """
    This function prints someone's name.
    """
    if isinstance(name, str):
        print(name)
    else:
        print(name, "is not a string")


# By placing ? and ?? after any function name will open up a window showing the Document string(Docstring) and the implementation of that function respectively.

# In[55]:


get_ipython().run_line_magic('pinfo', 'printName')


# In[59]:


get_ipython().run_line_magic('pinfo2', 'printName')


# help(function name) will print the Docstring of a function.

# In[42]:


help(printName)


# In python, a function always returns a value.

# In[81]:


print(printName("Samiur"))
print(type(printName("Taha")))


# In[86]:


def printValue(v2, v3, v1):
    print("v1 =", v1)
    print("v2 =", v2)
    print("v3 =", v3)

printValue(v2 = 'H', v3 = 5, v1 = 3.4)


# Also, a function can return multiple values.

# In[82]:


def returnValue():
    return a, b, a+b

a, b = 3, 5.7
a, b, sum = returnValue()
print("a =", a)
print("b =", b)
print("sum =", sum)


# In[84]:


def myAdd(*args):
    sum = 0
    for i in range(len(args)):
        sum += args[i]
    return sum

print("Sum =", myAdd(3, 4, 6))


# In[114]:


def printVariablesAndValues(**args):
    for x in args:
        print(x, "=", args[x])
        
printVariablesAndValues(a = 3, b = 'B', c = 2-3j, d = 6.3)


# We can assign default values to function arguments.

# In[118]:


def fun(x = 4):
    print("x =", x)
    
fun()
fun(10)
fun()


# In[119]:


def printList(L = [1, 2, 3]):
    print(L)
 
L = [6, 7, 8]
printList()
printList(L)
printList()


# ### Modules
# Modules are python files that contains some code that we want to use in several different projects. To use any segment of that code we have to import the whole module. To use the modules we need to specify the path where the module resides.

# In[19]:


import sys     #this is a system module
sys.path.append("C:/Users/Lanja Lan/Documents/Codes/Python")
import MyModule as m
print(m.addAllNumerics(2, 3, 4, 6))
print(m.courseName)


# We can alsp import one or multiple functions from a module.

# In[22]:


from MyModule import isNumeric
print(isNumeric(2, 3, 4, 'a'))


# If the modules are arranged in a directory structure, that directory structure is sometimes called package.

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')
import math

titanic_data = pd.read_csv("Titanic.csv")
titanic_data.head(10)

