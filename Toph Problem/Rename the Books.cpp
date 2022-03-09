#include <iostream>
using namespace std;
typedef long long int ll;
int main()
{
    int tc;
    cin>>tc;
    cin.ignore();
    while(tc--)
    {
        string a;
        getline(cin,a);
        int i,n=a.size();
        for(i=0;i<n;)
        {
            char ch=a[i];
            cout<<a[i];
            while(i<n && a[i]==ch)
                i++;
        }
        cout<<endl;
    }
}
