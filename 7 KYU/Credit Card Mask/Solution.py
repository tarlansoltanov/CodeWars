# Author : tarlansoltanov
# Name : Credit Card Mask
# ID : 5412509bd436bd33920011bc
# Link : https://www.codewars.com/kata/5412509bd436bd33920011bc
# Level : 7 KYU
# Language : Python

def maskify(cc):
    a = len(cc)-4
    b = cc[-4:]
    return('#'*a + b)