# Author : tarlansoltanov
# Name : Human Readable Time
# ID : 52685f7382004e774f0001f7
# Link : https://www.codewars.com/kata/52685f7382004e774f0001f7
# Level : 5 KYU
# Language : Python

def make_readable(s):
    return f"{s//3600:02d}:{s%3600//60:02d}:{s%60:02d}"