#include<iostream>

using namespace std;

int main()
{
    int n,cpul,meml,i;
    cin>>n>>cpul>>meml;
    int d[n],cpu[n],mem[n];

    for(i=0;i<n;i++)
    {
        cin>>d[i]>>cpu[i]>>mem[i];
    }
    int cle=0,mle=0,wa=0;
    for(i=0;i<n;i++)
    {
        if(cpu[i]>cpul)
        {
            cle=1;
            break;
        }
        if(mem[i]>meml)
        {
            mle=1;
            break;
        }
        if(d[i]!=0)
        {
            wa=1;
            break;
        }
    }

    if(cle)
        cout<<"CLE"<<endl;
    else if(mle)
        cout<<"MLE"<<endl;
    else if(wa)
        cout<<"WA"<<endl;
    else
        cout<<"AC"<<endl;

}
