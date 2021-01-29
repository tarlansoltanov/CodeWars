# Author : tarlansoltanov
# Name : Disemvowel Trolls
# ID : 52fba66badcd10859f00097e
# Link : https://www.codewars.com/kata/52fba66badcd10859f00097e
# Level : 7 KYU
# Language : Python

def disemvowel(string):
    string1 = ""
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    for i in string:
        if i not in vowel:
            string1+=i
    return string1