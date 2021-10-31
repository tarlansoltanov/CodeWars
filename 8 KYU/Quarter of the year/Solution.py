# Author : tarlansoltanov
# Name : Quarter of the year
# ID : 5ce9c1000bab0b001134f5af
# Link : https://www.codewars.com/kata/5ce9c1000bab0b001134f5af
# Level : 8 KYU
# Language : Python

def quarter_of(month):
    return month//3+int(month%3 != 0)s