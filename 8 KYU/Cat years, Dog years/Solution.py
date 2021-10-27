# Author : tarlansoltanov
# Name : Cat years, Dog years
# ID : 5a6663e9fd56cb5ab800008b
# Link : https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b
# Level : 8 KYU
# Language : Python

def human_years_cat_years_dog_years(h):
    return [h, 24+4*(h-2),24+5*(h-2)] if h > 1 else [h, 15, 15]