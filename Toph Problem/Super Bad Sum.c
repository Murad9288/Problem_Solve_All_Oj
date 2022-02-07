#include <bits/stdc++.h>
using namespace std;

#define sf scanf
#define pf printf
#define ssf sscanf
#define spf sprintf
#define fsf fscanf
#define fpf fprintf
#define fast ios_base::sync_with_stdio(0),cin.tie(0),cout.tie(0)
#define scase sf ("%d",&tc)
#define sn sf ("%d",&n)
#define whilecase while (tc--)
#define eof while (cin >> n)
#define forloop for (pos=1; pos<=tc; pos++)
#define arrayloop (i=0; i<n; i++)
#define cinstr cin >> str
#define getstr getline (cin,str)
#define pcase pf ("Case %d: ",pos)
#define pii pair <int,int>
#define pb push_back
#define in insert
#define llu unsigned long long
#define lld long long
#define U unsigned int
#define endl "\n"

const int MOD = 1000000007;
const int MAX = 1000005;

int badSum (int n)
{
    int sum = 0,rem;

    while (n)
    {
        rem = n % 10;

        if (rem & 1)
            sum += rem;

        n /= 10;
    }

    return sum;
}

int main (void)
{
    /*
    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);
    */

    int tc,n,sum;

    sf ("%d",&tc);

    while (tc--)
    {
        sf ("%d",&n);

        if (n > 1)
            sum = 1;
        else
            sum = 0;

        sum += badSum (n);

        for (int i=2; i*i<=n; i++)
        {
            if (n % i == 0)
            {
                sum += badSum(i);

                if (i * i != n)
                    sum += badSum(n/i);
            }
        }

        pf ("%d\n",sum);
    }

    return 0;
}
