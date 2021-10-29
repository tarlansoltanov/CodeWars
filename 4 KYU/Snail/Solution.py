# Author : tarlansoltanov
# Name : Snail
# ID : 521c2db8ddc89b9b7a0000c1
# Link : https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
# Level : 7 KYU
# Language : Python

def round(map, k, n):
    ans = []
    for i in range(k,n):
        ans.append(map[k][i])
    for i in range(k+1,n):
        ans.append(map[i][n-1])
    for i in range(n-2,k-1,-1):
        ans.append(map[n-1][i])
    for i in range(n-2,k,-1):
        ans.append(map[i][k])
    return ans

def snail(snail_map):
    ans = []
    k = 0
    n = len(snail_map[0])
    while k+1 <= n:
        ans += round(snail_map, k, n)
        k += 1
        n -= 1
    return ans
    