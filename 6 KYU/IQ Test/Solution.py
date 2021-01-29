# Author : tarlansoltanov
# Name : IQ Test
# ID : 552c028c030765286c00007d
# Link : https://www.codewars.com/kata/552c028c030765286c00007d
# Level : 6 KYU
# Language : Python

def iq_test(numbers):
    ans = [int(elem)%2 for elem in numbers.split(' ')]
    return(ans.index(0)+1 if ans.count(0)==1 else ans.index(1)+1)