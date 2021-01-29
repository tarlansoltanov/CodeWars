# Author : tarlansoltanov
# Name : Averages of numbers
# ID : 57d2807295497e652b000139
# Link : https://www.codewars.com/kata/57d2807295497e652b000139
# Level : 7 KYU
# Language : Python

def averages(arr):
    if arr:
        return list([(arr[i]+arr[i+1])/2 for i in range(0, len(arr)-1)])    
    return []