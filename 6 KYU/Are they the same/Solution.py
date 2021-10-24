# Author : tarlansoltanov
# Name : Are they the "same"?
# ID : 550498447451fbbd7600041c
# Link : https://www.codewars.com/kata/550498447451fbbd7600041c
# Level : 6 KYU
# Language : Python

def comp(array1, array2):
    return sorted(i**2 for i in array1) == sorted(array2) if array1 != [] and array2 != [] else array1 == array2
	