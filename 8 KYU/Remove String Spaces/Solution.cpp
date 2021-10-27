// Author : tarlansoltanov
// Name : Remove String Spaces
// ID : 57eae20f5500ad98e50002c5
// Link : https://www.codewars.com/kata/57eae20f5500ad98e50002c5
// Level : 8 KYU
// Language : C++

#include<bits/stdc++.h>

using namespace std;

string no_space(std::string x)
{
    string ans = "";
    for(int i = 0; i < x.length(); i++){
      if(x[i] != ' ') { ans += x[i]; }
    }
    return ans;
}