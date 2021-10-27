# Author : tarlansoltanov
# Name : Error correction #1 - Hamming Code
# ID : 5ef9ca8b76be6d001d5e1c3e
# Link : https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e
# Level : 6 KYU
# Language : Python

def encode(string):
    return ''.join([j*3 for i in string for j in str("{0:b}".format(ord(i)).zfill(8)) ])

def decode(bits):
    ascii = ''.join(["0" if bits[i:i+3].count('0')>1 else "1" for i in range(0, len(bits), 3)])
    return ''.join([chr(int(ascii[i:i+8],2)) for i in range(0, len(ascii), 8)])