# Author : tarlansoltanov
# Name : Sum of two lowest positive integers
# ID : 558fc85d8fd1938afb000014
# Link : https://www.codewars.com/kata/558fc85d8fd1938afb000014
# Level : 7 KYU
# Language : Python

def sum_two_smallest_numbers(numbers):
    ans = min(numbers)
    numbers.remove(ans)
    ans += min(numbers)
    return ans