# Sieve of Eratosthenes
# prim numbers as prim_num

import math

# Function which checks if x element is in a list
def contains(list, x):    # Can be list ar array
    for i in range(0, list.__len__()):
        a = list[i]
        if a == x:
            return 1
    return 0

# Function returns list of prime numbers less or equal to n
def erastothenes(n): # We are creating list/array of numbers
    prim_num = []

    for i_index in range(2, n):
        prim_num.append(i_index)

    for i_number in prim_num:
        for i_multiplier in range(2, int(math.sqrt(n))):
            multi = i_number * i_multiplier

            if contains(prim_num, multi):
                index = prim_num.index(multi)
                prim_num[index] = 0
    while contains(prim_num, 0):
        prim_num.remove(0)

    return prim_num

print(erastothenes(100))



