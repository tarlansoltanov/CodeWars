# Author : tarlansoltanov
# Name : k-Primes
# ID : 5726f813c8dcebf5ed000a6b
# Link : https://www.codewars.com/kata/5726f813c8dcebf5ed000a6b
# Level : 5 KYU
# Language : Python

def prime_factors(n):
    if n == 0:
        return 0
    c = 0
    while n%2 == 0:
        n //= 2
        c += 1
    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0:
            n //= i
            c += 1
    if n > 2:
        c += 1
    return c

def count_Kprimes(k, start, end):
    arr = []

    for i in range(start, end+1):
        if prime_factors(i) == k:
            arr.append(i)

    return arr

def puzzle(s):
    ans = 0
    p7 = [i for i in range(s) if prime_factors(i) == 7]

    for i in p7:
        k = s - i
        p3 = [j for j in range(k) if prime_factors(j) == 3]
        for j in p3:
            if prime_factors(k - j) == 1:
                ans += 1
    return ans