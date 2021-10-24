# Author : tarlansoltanov
# Name : Array.diff
# ID : 523f5d21c841566fde000009
# Link : https://www.codewars.com/kata/523f5d21c841566fde000009
# Level : 6 KYU
# Language : Python

def array_diff(a, b):
    return [i for i in a if i not in b]