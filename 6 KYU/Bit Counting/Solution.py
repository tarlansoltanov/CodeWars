# Author : tarlansoltanov
# Name : Bit Counting
# ID : 526571aae218b8ee490006f4
# Link : https://www.codewars.com/kata/526571aae218b8ee490006f4
# Level : 6 KYU
# Language : Python

def countBits(n):
    return(str(bin(n)).count("1"))