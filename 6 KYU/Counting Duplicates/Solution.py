# Author : tarlansoltanov
# Name : Counting Duplicates
# ID : 54bf1c2cd5b56cc47f0007a1
# Link : https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
# Level : 6 KYU
# Language : Python

def duplicate_count(text):
    text = text.lower()
    a = set(text)
    ans = 0
    for i in a:
        if text.count(i) > 1:
            ans += 1
    return ans