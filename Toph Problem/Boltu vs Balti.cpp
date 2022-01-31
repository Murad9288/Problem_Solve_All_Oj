#include <bits/stdc++.h>
using namespace std;

#define sf scanf
#define pf printf
#define scase sf ("%d",&tc)
#define sn sf ("%d",&n)
#define whilecase while (tc--)
#define eof while (cin >> n)
#define forloop for (pos=1; pos<=tc; pos++)
#define arrayloop (i=0; i<n; i++)
#define cinstr cin >> str
#define getstr getline (cin,str)
#define pcase pf ("Case %d: ",pos)
#define pb push_back
#define in insert
#define llu unsigned long long
#define lld long long
#define u unsigned int

int main (void)
{
    double x,y,res;
    while (cin >> x >> y)
    {
        if (x > y)
            swap (x,y);
        res = ((x+y)*(y-x+1))/2;
        pf ("Sum of %0.lf to %0.lf is -> %0.lf;\n",x,y,res);
    }
    return 0;
}
