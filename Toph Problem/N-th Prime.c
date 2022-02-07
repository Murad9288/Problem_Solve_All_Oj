#include<bits/stdc++.h>
using namespace std;
const int n=1e7;      //0=is prime.
bool isPrime[n];      //1= is not prime. In a global variable, every element=0 by default
int main()
{
  int k,counter=1;
  cin>>k;
  for (int i=3; i*i<=n; i+=2) //Loop running through only odd numbers
  {
    if (!isPrime[i])
    {
      for (int j=i*i; j<=n; j+=i)
      {
        isPrime[j]=1;
      }
    }
  }
  for (int i=3; i<=n; i+=2) //Loop running through only odd numbers
  {
    if (k==1) {cout<<2; break;}
    if (!isPrime[i])
    {
      counter++;
      if (k==counter) {cout<<i<<'\n'; break;}
    }
  }


  return 0;
}
