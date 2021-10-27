// Author : tarlansoltanov
// Name : Reversed Words
// ID : 51c8991dee245d7ddf00000e
// Link : https://www.codewars.com/kata/51c8991dee245d7ddf00000e
// Level : 8 KYU
// Language : C++

#include<bits/stdc++.h>

using namespace std;

vector<std::string> wordlist;

string reverse_words(const string& str) {
  stringstream ss(str);
  string ans = "";
  string word;
  while (ss >> word) {
    wordlist.push_back(word);
  }
  reverse(wordlist.begin(), wordlist.end());
  for(auto i = wordlist.begin(); i < wordlist.end(); i++){
      if(i+1 != wordlist.end()){
        ans += *i + " ";
      }
      else{
        ans += *i;
      }
  }
  wordlist.clear();
  return ans;
}