#!/usr/bin/env python
# coding: utf-8

# # CECS 229 Programming Assignment #3
# 
# #### Due Date: 
# 
# Sunday, 3/5 @ 11:59 PM
# 
# #### Submission Instructions:
# 
# To receive credit for this assignment you must submit to CodePost this file converted to a Python script named `pa3.py`
# 
# #### Objectives:
# 
# 1. Find the inverse of a given integer under a given modulo m.
# 2. Encrypt and decrypt text using an affine transformation.
# 3. Encrypt and decrypt text using the RSA cryptosystem.
# 
# 
# 
# 
# ### Programming Tasks
# 
# You may use the utility functions at the end of this notebook to aid you in the implementation of the following tasks:

# -------------------------------------------
# 
# #### Problem 1: 
# Create a function `modinv(a,m)` that returns the smallest, positive inverse of `a` modulo `m`.  If the gcd of `a` and `m` is not 1, then you must raise a `ValueError` with message `"The given values are not relatively prime"`.  You may NOT use any built-in functions as part of your implementation, but you may use any functions you implemented in previous coding assignments.  Please make sure to copy and paste them into this file, so that they are uploaded to CodePost when you submit your `pa3.py` file.

# In[21]:


def bezout_coeffs(a, b):
    if b == 0:
        return {a : 1, b : 0}
    s, o_s = 0, 1
    t, o_t = 1, 0
    
    r,o_r = b, a
    
    while r != 0:
        q = o_r // r
        o_r, r = r, o_r - q * r
        o_s, s = s, o_s - q * s
        o_t, t = t, o_t - q * t
        
    return {a: o_s, b: o_t}

def gcd(a,b):
    f = bezout_coeffs(a, b)
    sa = a*(list(f.values())[0])
    tb = b*(list(f.values())[1])
    final = sa + tb
    if final < 0:
        final = -1*(sa + tb)
    return final

def modinv(a,m):
    if gcd(a, m) != 1:
        raise ValueError
    
    c = bezout_coeffs(a, m)
    inv = c[a]
    
    while inv < 0 or inv > m-1:
        if inv < 0:
            inv += m
            
        elif inv > m-1:
            inv -= m
            
    return inv

    """returns the smallest, positive inverse of a modulo m
    INPUT: a - integer
           m - positive integer
    OUTPUT: an integer in the range [0, m-1]
    """


# In[24]:


#print(modinv(2, 4))


# ------------------------------------
# 
# #### Problem 2: 
# Create a function `affineEncrypt(text, a,b)` that returns the cipher text encrypted using key  (`a`, `b`).  You must verify that the gcd(a, 26) = 1 before making the encryption.  If this is not the case, the function must raise a `ValueError` with message `"The given key is invalid. The gcd(a,26) must be 1."`.  You may NOT use any built-in functions as part of your implementation, but you may use any functions you implemented in previous coding assignments.  Please make sure to copy and paste them into this file, so that they are uploaded to CodePost when you submit your `pa3.py` file.

# In[14]:


def digits2letters(digits):
    letters = ""
    start = 0  #initializing starting index of first digit
    while start <= len(digits) - 2:
        digit = digits[start : start + 2]  # accessing the double digit
        letters += chr( int(digit) +65)   # concatenating to the string of letters
        start += 2                         # updating the starting index for next digit
    return letters

def letters2digits(letters):
    digits = ""
    for c in letters:
        if c.isalpha():
            letter = c.upper()  #converting to uppercase  
            d = ord(letter)-65
            if d < 10:
                digits += "0" + str(d)     # concatenating to the string of digits
            else:
                digits += str(d)
    return digits

def affineEncrypt(text, a, b):
    """encrypts the plaintext 'text', using an affine transformation key (a, b)
    INPUT:  text - plaintext as a string of letters
            a - integer satisfying gcd(a, 26) = 1.  Raises error if such is not the case
            b - integer 
            
    OUTPUT: The encrypted message as a string of characters
    """
    if gcd(a, 26) != 1:
        raise ValueError("The given key is invalid")
    else:
        num = ""
        text = text.replace(" ", "")
        for char in text:
            d = letters2digits(char)
            d = (a * int(d) + b) % 26 
            
            if d < 10:
                num += "0" 
                num += str(d)
            else:
                num += str(d)
        cipher = digits2letters(num)
        return cipher    


# In[ ]:





# #### Problem 3: 
# Create a function `affineDecrypt(ciphertext, a,b)` that returns the cipher text encrypted using key  (`a`, `b`). You must verify that the gcd(a, 26) = 1.  If this is not the case, the function must raise `ValueError` with message `"The given key is invalid. The gcd(a,26) must be 1."`.  You may NOT use any built-in functions as part of your implementation, but you may use any functions you implemented in previous coding assignments.  Please make sure to copy and paste them into this file, so that they are uploaded to CodePost when you submit your `pa3.py` file.

# In[101]:


def bezout_coeffs(a, b):
    if b == 0:
        return {a : 1, b : 0}
    s, o_s = 0, 1
    t, o_t = 1, 0
    
    r,o_r = b, a
    
    while r != 0:
        q = o_r // r
        o_r, r = r, o_r - q * r
        o_s, s = s, o_s - q * s
        o_t, t = t, o_t - q * t
        
    return {a: o_s, b: o_t}

def gcd(a,b):
    f = bezout_coeffs(a, b)
    sa = a*(list(f.values())[0])
    tb = b*(list(f.values())[1])
    final = sa + tb
    if final < 0:
        final = -1*(sa + tb)
    return final

def modinv(a,m):
    if gcd(a, m) != 1:
        raise ValueError
    
    c = bezout_coeffs(a, m)
    inv = c[a]
    
    while inv < 0 or inv > m-1:
        if inv < 0:
            inv += m
            
        elif inv > m-1:
            inv -= m
            
    return inv

def digits2letters(digits):
    letters = ""
    start = 0  #initializing starting index of first digit
    while start <= len(digits) - 2:
        digit = digits[start : start + 2]  # accessing the double digit
        letters += chr( int(digit) +65)   # concatenating to the string of letters
        start += 2                         # updating the starting index for next digit
    return letters

def letters2digits(letters):
    digits = ""
    for c in letters:
        if c.isalpha():
            letter = c.upper()  #converting to uppercase  
            d = ord(letter)-65
            if d < 10:
                digits += "0" + str(d)     # concatenating to the string of digits
            else:
                digits += str(d)
    return digits

def affineDecrypt(ciphertext, a, b):
    """decrypts the string 'ciphertext', which was encrypted using an affine transformation key (a, b)
    INPUT:  ciphertext - a string of encrypted letters
            a - integer satisfying gcd(a, 26) = 1.  
            b - integer 
            
    OUTPUT: The decrypted message as a string of characters
    """
    text = ''
    if gcd(a, 26) != 1:
        raise ValueError("The given key is invalid")
    else:
        num = ""
        for char in ciphertext:
            d = letters2digits(char)
            inverse = modinv(a, 26)
            d = (inverse * (int(d) - b)) % 26
            
            if d < 10:
                num += '0'
                num += str(d)
            else:
                num += str(d)
                
        result = digits2letters(num)
        return result


# In[102]:


print(affineDecrypt("YTSNNSHHOTWSX", 21, 10))


# -----------------------------------
# 
# #### Problem 4:
# 
# Implement the function `encryptRSA(message, n, e)` which encrypts a string `message` using RSA key `(n = p * q, e)`.  You may NOT use any built-in functions as part of your implementation, but you may use any functions you implemented for previous coding assignments.  Please make sure to copy and paste them into this file, so that they are uploaded to CodePost when you submit your `pa3.py` file.

# In[65]:


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

def blocksize(n):
    """returns the size of a block in an RSA encrypted string"""
    twofive = "25"
    while int(twofive) < n:
        twofive += "25"
    return len(twofive) - 2
    


def encryptRSA(message, n, e):
    """encrypts the plaintext message, using RSA and the key (n = p * q, e)
    INPUT:  message - plaintext as a string of letters
            n - a positive integer
            e - integer satisfying gcd((p-1)*(q-1), e) = 1
            
    OUTPUT: The encrypted message as a string of digits
    """
    s = blocksize(n)
    
    message = message.replace(" ", "")
    while (len(message)*2) % s != 0:
        message += 'X'
        
    d = letters2digits(message)

    list = []

    t = ""
    for i in d:
        t += i
        if len(t) == s:
            list.append(t)
            t = ""
        
    fin = ""
    for i in range(0, len(list)):
        z = str(mod_exp(int(list[i]), e, n))
        
        if len(z) < s:
            zeros = s - len(z)
            fin += ('0'*zeros)
            fin += z + " "
        else:
            fin += z + " "
            
    return fin
    


# In[67]:


"""--------------------- ENCRYPTION TESTER CELL ---------------------------"""
encrypted1 = encryptRSA("STOP", 2537, 13)
encrypted2 = encryptRSA("HELP", 2537, 13)
encrypted3 = encryptRSA("STOPS", 2537, 13)
print("Encrypted Message:", encrypted1)
print("Expected: 2081 2182")
print("Encrypted Message:", encrypted2)
print("Expected: 0981 0461")
print("Encrypted Message:", encrypted3)
print("Expected: 2081 2182 1346")


"""--------------------- TEST 2 ---------------------------"""
encrypted = encryptRSA("UPLOAD", 3233, 17)
print("Encrypted Message:", encrypted)
print("Expected: 2545 2757 1211")


# -------------------------------------------------------
# 
# #### Problem 5:
# 
# Complete the implementation of the function `decryptRSA(c, p, q, m)` which depends on `modinv(a,m)` and the given functions `digits2letters(digits)` and `blockSize(n)`.  When you are done, you can test your function against the given examples.

# In[73]:


def blocksize(n):
    """returns the size of a block in an RSA encrypted string"""
    twofive = "25"
    while int(twofive) < n:
        twofive += "25"
    return len(twofive) - 2
def bezout_coeffs(a, b):
    if b == 0:
        return {a : 1, b : 0}
    s, o_s = 0, 1
    t, o_t = 1, 0
    
    r,o_r = b, a
    
    while r != 0:
        q = o_r // r
        o_r, r = r, o_r - q * r
        o_s, s = s, o_s - q * s
        o_t, t = t, o_t - q * t
        
    return {a: o_s, b: o_t}

def gcd(a,b):
    f = bezout_coeffs(a, b)
    sa = a*(list(f.values())[0])
    tb = b*(list(f.values())[1])
    final = sa + tb
    if final < 0:
        final = -1*(sa + tb)
    return final

def modinv(a,m):
    if gcd(a, m) != 1:
        raise ValueError
    
    c = bezout_coeffs(a, m)
    inv = c[a]
    
    while inv < 0 or inv > m-1:
        if inv < 0:
            inv += m
            
        elif inv > m-1:
            inv -= m
            
    return inv

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

def decryptRSA(cipher, p, q, e):
    """decrypts cipher, which was encrypted using the key (p * q, e)
    INPUT:  cipher - ciphertext as a string of digits
            p, q - prime numbers used as part of the key n = p * q to encrypt the ciphertext
            e - integer satisfying gcd((p-1)*(q-1), e) = 1
            
    OUTPUT: The decrypted message as a string of letters
    """
     
    cipher = cipher.replace(" ", "")
    s = blocksize(p * q)
    
    list = []
    
    inverse = modinv(e, (p-1)*(q-1))
    first = ""
    for i in cipher:
        first += i
        if len(first) == s:
            list.append(first)
            first = "" 
            
    result = ""
    for i in range(0, len(list)):
        z = str(mod_exp(int(list[i]), inverse, p*q))
        
        if len(z) < s:
            zeros = s - len(z)
            result += ("0" * zeros)
            result += z
        else:
            result += z
            
    out = ""
    out += digits2letters(result)
    return out


# In[74]:


"""--------------------- TESTER CELL ---------------------------"""
decrypted1 = decryptRSA("2081 2182", 43, 59, 13)
decrypted2 = decryptRSA("0981 0461", 43, 59, 13)
decrypted3 = decryptRSA("2081 2182 1346", 43, 59, 13)
print("Decrypted Message:", decrypted1)
print("Expected: STOP")
print("Decrypted Message:", decrypted2)
print("Expected: HELP")
print("Decrypted Message:", decrypted3)
print("Expected: STOPSX")

"""--------------------- TEST 2---------------------------"""
decrypted = decryptRSA("0667 1947 0671", 43, 59, 13)
print("Decrypted Message:", decrypted)
print("Expected: SILVER")


# ------------------------------------------
# ##### Utility functions (NO EDITS NECESSARY)

# In[1]:





# In[2]:





# In[ ]:


def digits2letters(digits):
    letters = ""
    start = 0  #initializing starting index of first digit
    while start <= len(digits) - 2:
        digit = digits[start : start + 2]  # accessing the double digit
        letters += chr( int(digit) +65)   # concatenating to the string of letters
        start += 2                         # updating the starting index for next digit
    return letters
    


# In[ ]:


def letters2digits(letters):
    digits = ""
    for c in letters:
        if c.isalpha():
            letter = c.upper()  #converting to uppercase  
            d = ord(letter)-65
            if d < 10:
                digits += "0" + str(d)     # concatenating to the string of digits
            else:
                digits += str(d)
    return digits


# In[ ]:


def blocksize(n):
    """returns the size of a block in an RSA encrypted string"""
    twofive = "25"
    while int(twofive) < n:
        twofive += "25"
    return len(twofive) - 2

