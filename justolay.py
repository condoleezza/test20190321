# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def inc(x):
    def incx(y):
        return x + y
    return incx

inc2 = inc(2)
inc5 = inc(5)

def innc(x):
    def innc2(y):
        def innc3(z):
            return x + y + z
        return innc3
    return innc2

num = [2,-5,9,7,-2,5,3,1,0,-3,8]
positive_num = filter(lambda x:x>0,num)
#average = reduce(lambda x,y:x+y,positive_num) / len(positive_num)

import numpy as np
import random
def rand10():
    while True:
        a1 = random.randint(1,7) - 1
        a2 = random.randint(1,7) - 1
        r = 7 * a1 + a2
        if r < 10:
            break
    return r + 1

nums = []
for i in range(1000000):
    nums.append(rand10())

for i in range(10):
    print(nums.count(i+1) / len(nums))
    print('\n')    

 #Monte Carlo simulation
def circle():
    a = random.random() ** 2
    b = random.random() ** 2
    distance = a + b
    return distance ** 0.5

import time
import numpy as np
import random
start_points = time.time()
points = 0
length = 1000000000
for i in range(length):
    r = circle()
    if r < 1:
        if i % 1000000 == 0:
            print(i)
        points += 1
calc_pi = points * 4 / length
end_points = time.time()
interval = end_points - start_points 
print(calc_pi)
print(interval)