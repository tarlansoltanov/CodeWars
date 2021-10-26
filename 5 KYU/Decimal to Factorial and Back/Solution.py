# Author : tarlansoltanov
# Name : Decimal to Factorial and Back
# ID : 54e320dcebe1e583250008fd
# Link : https://www.codewars.com/kata/54e320dcebe1e583250008fd
# Level : 5 KYU
# Language : Python

def fac(n):
    if n == 0:
        return 0
    return n * fac(n-1) if n != 1 else 1


def dec_2_fact_string(nb):
    arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans  = ""
    n = 1
    while nb != 0:
        ans = arr[nb % n] + ans
        nb //= n
        n += 1
    return ans
    

def fact_string_2_dec(string):
    arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = 0
    for i in range(len(string)):
        k = len(string) - i - 1
        ans += fac(k) * arr.index(string[i])
    return ans