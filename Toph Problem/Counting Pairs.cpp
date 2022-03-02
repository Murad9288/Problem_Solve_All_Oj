#include<bits/stdc++.h>
#define ll              long long
#define ull             unsigned long long
#define pb              push_back
#define fastread()      (ios_base:: sync_with_stdio(false),cin.tie(NULL));
using namespace std;
int main()
{
    fastread();
    ll t,n,a[1001],test = 1;
    cin>>t;
    while(t--){
        cin>>n;
        for(int i=0; i<n; i++){
            cin>>a[i];
        }
        sort(a,a+n);
        ll ans = 0,sum  = 0;
        for(int i=0; i<n; i++){
            for(int j=i+1; j<n; j++){
                sum = a[i] + a[j];
                if(sum % 5 == 0){
                    ans++;
                }
            }
        }
        cout<<"Case "<<test<<": "<<ans<<endl;
        test++;
    }

    return 0;
}
