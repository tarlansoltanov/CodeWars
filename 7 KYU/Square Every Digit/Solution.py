# Author : tarlansoltanov
# Name : Square Every Digit
# ID : 546e2562b03326a88e000020
# Link : https://www.codewars.com/kata/546e2562b03326a88e000020
# Level : 7 KYU
# Language : Python

def square_digits(num):
    return int("".join([str(int(i)*int(i)) for i in str(num)]))