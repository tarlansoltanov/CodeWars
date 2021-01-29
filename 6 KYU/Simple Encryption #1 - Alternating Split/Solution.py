# Author : tarlansoltanov
# Name : Simple Encryption #1 - Alternating Split
# ID : 57814d79a56c88e3e0000786
# Link : https://www.codewars.com/kata/57814d79a56c88e3e0000786
# Level : 6 KYU
# Language : Python

def decrypt_one(text):
    mid=int(len(text)/2)
    decry_one = text[0:mid]
    decry_two = text[mid:]
    s=""
    for i in range(0,mid):
        s += decry_two[i]+decry_one[i]
    if len(text)%2!=0:
        s += decry_two[mid]
    return s


def decrypt(encrypted_text, n):
    if n < 0:
        return encrypted_text
    s=[encrypted_text]
    for i in range(0,n):
        s.append(decrypt_one(s[i]))
    return s[n]


def encrypt(text, n):
    for i in range(0,n):
        text=text[1::2]+text[::2]
    return(text)