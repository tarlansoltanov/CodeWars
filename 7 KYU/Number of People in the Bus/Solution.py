# Author : tarlansoltanov
# Name : Number of People in the Bus
# ID : 5648b12ce68d9daa6b000099
# Link : https://www.codewars.com/kata/5648b12ce68d9daa6b000099
# Level : 7 KYU
# Language : Python

def number(bus_stops):
    return sum([(a-b) for a,b in bus_stops])