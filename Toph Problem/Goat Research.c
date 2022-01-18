#include<iostream>

using namespace std;

int main()
{

    int n,i,j;
    cin>>n;
   string s[n];
    for(i=0;i<n;i++)
        cin>>s[i];

    int maxLen = s[0].size();
    for(i=0;i<n;i++)
    {
        int l = s[i].size();
        if(l>maxLen)
            maxLen = l;
    }
 

    for(i=0;i<n;i++)
    {
        int len = s[i].size();
        int t = len;
        len-=1;
        if(len%2==1)
        {
            if(len-1==0)
                len+=1;
            else
                len-=1;
        }

        for(j=0;j<(maxLen-len-1)/2;j++)
            cout<<" ";
            cout<<"b";
        for(j=0;j<len;j++)
            cout<<"a";

        cout<<endl;


    }


}
