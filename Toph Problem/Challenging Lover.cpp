#include<iostream>
using namespace std;
int main()
{
    int t,s,c,i;
    long long int n;
    cin>>t;
    while(t--)
    {
        cin>>n;
        s=c=0;
        for(i=1; i<=n; i++)
        {
            if(n%i==0)
                s+=i;
        }
        for(i=1; i<=s; i++)
        {
            if(s%i==0)
                c++;
        }
        if(c==2)
            cout<<"Yes"<<endl;
        else
            cout<<"No"<<endl;
    }
    return 0;
}
