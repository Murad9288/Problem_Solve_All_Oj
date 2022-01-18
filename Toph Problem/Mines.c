#include <bits/stdc++.h>
using namespace std;

using ll = long long;
char s[12][12];

int dx[] = {1, 0, -1, 0, 1, 1, -1, -1};
int dy[] = {0, 1, 0, -1, 1, -1, 1, -1};

int main() {
 ios_base::sync_with_stdio(0); cin.tie(0);

 int r, c,i,j,cnt=0,k;
 scanf("%d %d", &r, &c);
 for( i = 1; i <= r; i++)
  scanf(" %s", s[i] + 1);

 for( i = 1; i <= r; i++) {
  for( j = 1; j <= c; j++) {
   if(s[i][j] != '*') {
     cnt = 0;
    for( k = 0; k < 8; k++) {
     int tx = i + dx[k];
     int ty = j + dy[k];
     if(s[tx][ty] == '*')
      cnt++;
    }
    if(cnt) s[i][j] = (char)('0' + cnt);
    else s[i][j] = '.';
   }
  }
 }
 for( i = 1; i <= r; i++) {
  for( j = 1; j <= c; j++)
   printf("%c", s[i][j]);
  puts("");
 }
 return 0;
}
