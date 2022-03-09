#include<bits/stdc++.h>

using namespace std;

int main()
{


  int a,i;

  string s;

  cin>>a;

  while(a--){

        cin>>s;

     for(i=0;i<s.size();i++){

        if(tolower(s[i])==tolower(s[i-1])){
            cout<<"#";
            continue;
        }
        else{
            cout<<s[i];

        }


     }


 cout<<endl;


     }

}
