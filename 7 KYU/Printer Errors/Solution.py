# Author : tarlansoltanov
# Name : Printer Errors
# ID : 56541980fa08ab47a0000040
# Link : https://www.codewars.com/kata/56541980fa08ab47a0000040
# Level : 7 KYU
# Language : Python

def printer_error(s):
    ans = 0
    for i in s:
        if ord(i)>109:
            ans+=1
    return (str(ans) + '/' + str(len(s)))