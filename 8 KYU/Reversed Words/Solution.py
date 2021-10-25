# Author : tarlansoltanov
# Name : Reversed Words
# ID : 51c8991dee245d7ddf00000e
# Link : https://www.codewars.com/kata/51c8991dee245d7ddf00000e
# Level : 8 KYU
# Language : Python

def reverse_words(s):
    s = ' '.join(reversed(s.split(" ")))
    return s