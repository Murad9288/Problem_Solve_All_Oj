#include<iostream>
using namespace std;

int main()
{
    int n,m,i,j;
    cin>>n>>m;
    char s[n][m];

    for(i=0;i<n;i++)
        for(j=0;j<m;j++)
            cin>>s[i][j];

          int c=0;

   for(i=0;i<n;i++)
   {
       for(j=0;j<m;j++)
       {
           if(i==0&&j==0)
           {
               if(s[i][j]=='.'&&s[i][j+1]!='*'&&s[i+1][j]!='*')
                c++;
           }
           else if(j==0)
           {
               if(s[i][j]=='.'&&s[i][j+1]!='*'&&s[i+1][j]!='*'&&s[i-1][j]!='*')
                c++;
           }
           else if(j==m-1)
           {
               if(s[i][j]=='.'&&s[i][j-1]!='*'&&s[i+1][j]!='*'&&s[i-1][j]!='*')
                c++;
           }
           else if(i==0&&j==m-1)
           {
               if(s[i][j]=='.'&&s[i][j-1]!='*'&&s[i+1][j]!='*')
                c++;
           }
           else if(i==n-1&&j==0)
           {
               if(s[i][j]=='.'&&s[i][j+1]!='*'&&s[i-1][j]!='*')
                c++;
           }
           else if(i==n-1&&j==m-1)
           {
               if(s[i][j]=='.'&&s[i][j-1]!='*'&&s[i-1][j]!='*')
                c++;
           }
           else
           {
               if(s[i][j]=='.')
           {
             if(s[i][j+1]!='*'&&s[i][j-1]!='*'&&s[i-1][j]!='*'&&s[i+1][j]!='*')
                c++;
           }
           }

       }
   }

   cout<<c<<endl;
}
