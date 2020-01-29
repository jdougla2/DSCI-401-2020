# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:08:27 2020

@author: Katherine Lamb

Week 3
"""
#%%
print("~~~~~~~~Monday Notes~~~~~~~~")

#%pprint turns off pretty printing

#list all even numbers 1 - 100
print([x for x in range(1, 101) if x % 2 == 0])
print()
#or
print([2 * x for x in range(1, 51)])
print()

#list comprehension for tuples
print([(x, y) for x in range(1, 6) for y in range(1, 6)])
print()

#add two things in a tuple and get 100%
print([(x, y) for x in range (1, 101) for y in range(1, 101) if x + y == 100])
print()

#function that adds two numbers
def addition(x, y):
    return x + y
print(addition(69, 420))
print()

#function that adds two numbers and sometimes multiplies things or powers them
def fancy_addition(x, y, mult=1, pwr=1):
    return mult * (x + y) ** pwr
print(fancy_addition(17, 32, pwr=2, mult=-1))
print()

#unspecificed num of args
#puts every arg after b into a tuple
def something(a, b, *c):
    print(a)
    print(b)
    print(c)
something(1, 2, 3, 4, 5)
    
#more unspec num of args practice
def moar_practice(*inputs):
    print(inputs)
    return sum(inputs)

args = list(range(15))
print(moar_practice(*args))
#that turns the items in args into individual arguments

coords = [(x, y) for x in range(1, 6)[::-1] for y in range(1, 6)[::-1]]

#some different ways to sort things
print(sorted(coords, key=lambda x: x[0]))
print()
print(sorted(coords, key=lambda x: x[1]))
print()
print(sorted(coords, key=lambda x: x[0] + x[1]))

#if you have a funtion in another file you can import it by saying 
#from file_name_without_extension import function_name
#this is the easiest way to import functions for testing
#as if any of these students are going to do that

#random numbers
import random as rnd
print(rnd.random()) #radom uniform numbers 0 through 1
print(rnd.randint(1,5)) #random uniform ints 1 through 4
print(rnd.sample(list(range(1, 10)), 10))

#%%