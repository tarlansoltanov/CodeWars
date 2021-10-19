# Author : tarlansoltanov
# Name : Sum of Digits / Digital Root
# ID : 541c8630095125aba6000c00
# Link : https://www.codewars.com/kata/541c8630095125aba6000c00
# Level : 6 KYU
# Language : Python

def digital_root(n):
    return digital_root(sum([int(i) for i in str(n)])) if n // 10 else n 