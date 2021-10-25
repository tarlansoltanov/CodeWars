# Author : tarlansoltanov
# Name : Halving Sum
# ID : 5a58d46cfd56cb4e8600009d
# Link : https://www.codewars.com/kata/5a58d46cfd56cb4e8600009d
# Level : 7 KYU
# Language : Python

def halving_sum(n): 
    sum = n
    while n != 1:
        n //= 2
        sum += n
    return sum