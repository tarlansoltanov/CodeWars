# Author : tarlansoltanov
# Name : Your order, please
# ID : 55c45be3b2079eccff00010f
# Link : https://www.codewars.com/kata/55c45be3b2079eccff00010f
# Level : 6 KYU
# Language : Python

def order(n):
    n = list(n.split(" "))

    ans = {"1": "","2": "","3": "","4": "","5": "","6": "","7": "","8": "","9": ""}
    for i in ans.keys():
        for j in n:
            if i in j:
                ans[i] = j

    return(' '.join(elem for elem in ans.values()).strip())