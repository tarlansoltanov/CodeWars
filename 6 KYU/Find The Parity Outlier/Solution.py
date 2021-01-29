# Author : tarlansoltanov
# Name : Find The Parity Outlier
# ID : 5526fc09a1bbd946250002dc
# Link : https://www.codewars.com/kata/5526fc09a1bbd946250002dc
# Level : 6 KYU
# Language : Python

def find_outlier(integers):
    ans = [int(elem)%2 for elem in integers]
    return(integers[ans.index(0)] if ans.count(0)==1 else integers[ans.index(1)])