# Author : tarlansoltanov
# Name : Row Weights
# ID : 5abd66a5ccfd1130b30000a9
# Link : https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9
# Level : 7 KYU
# Language : Python

def row_weights(array):
    return sum(array[0::2]), sum(array[1::2])