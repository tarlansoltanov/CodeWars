# Author : tarlansoltanov
# Name : Get the Middle Character
# ID : 56747fd5cb988479af000028
# Link : https://www.codewars.com/kata/56747fd5cb988479af000028
# Level : 7 KYU
# Language : Python

def get_middle(s):
    if len(s)%2==0:
        return s[len(s)//2-1:len(s)//2+1]
    return s[len(s)//2]