# Author : tarlansoltanov
# Name : Rectangle into Squares
# ID : 55466989aeecab5aac00003e
# Link : https://www.codewars.com/kata/55466989aeecab5aac00003e
# Level : 6 KYU
# Language : Python

ans = []

def sqInRect(lng, wdth):
    global ans
    if lng==wdth:
        if not ans:
            return None
        ans.append(lng)
        x = ans
        ans = []
        return x
    elif lng > wdth:
        ans.append(wdth)
        return sqInRect(lng-wdth, wdth)
    elif lng < wdth:
        ans.append(lng)
        return sqInRect(lng, wdth-lng)