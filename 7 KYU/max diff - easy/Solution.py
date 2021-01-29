# Author : tarlansoltanov
# Name : max diff - easy
# ID : 588a3c3ef0fbc9c8e1000095
# Link : https://www.codewars.com/kata/588a3c3ef0fbc9c8e1000095
# Level : 7 KYU
# Language : Python

def max_diff(lst):
    if lst != []:
        return max(lst) - min(lst)
    return 0