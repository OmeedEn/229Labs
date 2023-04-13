#!/usr/bin/env python
# coding: utf-8

# # CECS 229: Programming Assignment #1
# 
# #### Due Date: 
# 
# Sunday, 2/5 @ 11:59 PM
# 
# #### Submission Instructions:
# 
# To receive credit for this assignment, you must submit **to CodePost** this file converted to a Python script named `pa1.py`
# 
# #### Objectives:
# 
# 1. Compute the quotient and remainder of two numbers.
# 2. Apply numerical algorithms for computing the sum of two numbers in binary representation.
# 3. Apply numerical algorithms for computing the modular exponentiation of a positive integer.
# 
# 

# --------------------------------
# 
# #### Problem 1:
# 
# Program a function `div_alg(a, d)` that computes the quotient and remainder of $$a \div d$$ according to the Division Algorithm (THM 4.1.2).   
# 
# The function should satisfy the following:
# 
# 1. INPUT: 
#     * `a` - an integer representing the dividend
#     * `d` - positive integer representing the divisor
# 
#     
# 2. OUTPUT:
#     * a dictionary of the form `{'quotient' : q, 'remainder' : r}` where `q` and `r` are the quotient and remainder values, respectively.  The remainder should satisfy, $0 \leq r < d$.
# 
#  
# EXAMPLE: 
# 
# `>> div_alg( 101 , 11 )`
# 
# `{'quotient' : 9, 'remainder' : 2}`

# In[28]:


def div_alg(a, d):
    list = ["quotient", "remainder"]
    dict = {}
    remainder = a % d
    quotient = a // d
    for i in list:
        dict[i] = None
    dict['quotient'] = quotient
    dict['remainder'] = remainder
    return dict
    


# --------------------------------
# 
# #### Problem 2:
# 
# Program a function `binary_add(a, b)` that computes the sum of the binary numbers  $$a = (a_{i-1}, a_{i-2}, \dots, a_0)_2$$ and $$b = (b_{j-1}, b_{j-2}, \dots, b_0)_2$$ using the algorithm discussed in lecture.  No credit will be given to functions that employ any other implementation.  The function can not use built-in functions that already perform some kind of binary representation or addition of binary numbers.  For example, the function implementation can **not** use the functions `bin()` or `int(a, base=2)`.
# 
# The function should satisfy the following:
# 
# 1. INPUT: 
#     * `a` - a string of the 0's and 1's that make up the first binary number.  The string *may* contain spaces.
#     * `b` - a string of the 0's and 1's that make up the first binary number.  The string *may* contain spaces.
# 
#     
# 2. OUTPUT:
#     * the string of 0's and 1's that is the result of computing $a + b$.  The string must be separated by spaces into blocks of 4 characters or less, beginning at the end of the string.
# 
#  
# EXAMPLE: 
# 
# `>> binary_add( '10 1011' , '11011')`
# 
# `'100 0110'`
# 
# 
# 

# In[8]:


def binary_add(a, b):
    a = a.replace(" ", "")
    b = b.replace(" ", "")
    res = ""
    c = 0
    k = max(len(a), len(b))
    a = a.zfill(k)
    b = b.zfill(k)
    alist = [int(i) for i in a]
    blist = [int(i) for i in b]
    s = [0] * k
    for i in range(k - 1, -1, -1):
        s[i] = ((alist[i]) + (blist[i]) + c) % 2
        c = ((alist[i]) + (blist[i]) + c) // 2
    if c == 1:
        s = [c] + s
    for i in range(len(s)):
        res += str(s[i])

    res = res[::-1]
    res = [res[i:i + 4] for i in range(0, len(res), 4)]
    res = " ".join(res)

    return res[::-1]

    


# --------------------------------
# 
# #### Problem 3:
# 
# Program a function `mod_exp(b, n, m)` that computes $$b^n \mod m$$ using the algorithm discussed in lecture.  No credit will be given to functions that employ any other implementation.  For example, if the function implementation simply consists of `b ** n % m`, no credit will be given.  
# 
# The function should satisfy the following:
# 
# 1. INPUT: 
#     * `b` - positive integer representing the base
#     * `n` - positive integer representing the exponent
#     * `m` - positive integer representing the modulo
# 
#     
# 2. OUTPUT:
#     * the computation of $b^n \mod m$ if b, n, m are positive integers, 0 otherwise.
# 
#  
# EXAMPLE: 
# 
# `>> mod_exp( 3 , 644, 645 )`
# 
# `36`
# 
# 
# 

# In[10]:


def mod_exp(b, n, m):
    if b < 0:
        return 0
    x = 1
    power = b % m
    while n > 0:
        if n%2 == 1:
            x = (x * power) % m
        n = n // 2
        power = (power * power) % m
    return x
    

