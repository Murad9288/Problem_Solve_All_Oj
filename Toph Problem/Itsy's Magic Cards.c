#include <bits/stdc++.h>

using namespace std;

bool check(vector<vector<int> > &g){
 for(auto i:g){
  for(auto j:i){
   if(j){
    return true;
   }
  }
 }
 return false;
}

int main() {
 int n, m;
 cin>>n>>m;
 vector<vector<int> > g(n, vector<int>(n, 0));
 for(int i=0;i<m;i++){
  char a, b;
  cin>>a>>b;
  g[a-'A'][b-'A']=1;
  g[b-'A'][a-'A']=1;
 }
 int res=n;
 while(check(g)){
  int mx=0, to=0;
  for(int i=0;i<n;i++){
   int cnt=0;
   for(auto j:g[i]){
    cnt+=j;
   }
   if(cnt>mx){
    mx=cnt;
    to=i;
   }
  }
  for(int i=0;i<n;i++){
   if(g[to][i]){
    g[to][i]=0;
    g[i][to]=0;
   }
  }
  res--;
 }
 cout<<res;
 return 0;
}
