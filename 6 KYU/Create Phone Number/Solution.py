# Author : tarlansoltanov
# Name : Create Phone Number
# ID : 525f50e3b73515a6db000b83
# Link : https://www.codewars.com/kata/525f50e3b73515a6db000b83
# Level : 6 KYU
# Language : Python

def create_phone_number(n):
    a = ''.join(str(elem) for elem in n)
    return "(" + a[0:3] + ") " + a[3:6] + "-" + a[6:]