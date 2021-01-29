// Author : tarlansoltanov
// Name : Bit Counting
// ID : 526571aae218b8ee490006f4
// Link : https://www.codewars.com/kata/526571aae218b8ee490006f4
// Level : 6 KYU
// Language : C++

unsigned int countBits(unsigned long long n){
  if(n==0){
    return 0;
  }
  return countBits((unsigned long long)n / 2) + n%2;
}