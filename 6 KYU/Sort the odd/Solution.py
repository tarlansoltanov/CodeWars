# Author : tarlansoltanov
# Name : Sort the odd
# ID : 578aa45ee9fd15ff4600090d
# Link : https://www.codewars.com/kata/578aa45ee9fd15ff4600090d
# Level : 6 KYU
# Language : Python

def sort_array(n):
    ans = []
    for i in n:
        if i%2==1:
            ans.append(i)
    ans.sort()
    k=0
    for i in range(0,len(n)):
        if n[i]%2==1:
            n[i] = ans[k]
            k+=1
    return n