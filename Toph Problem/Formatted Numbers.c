# Accepted:
# Language: C++

#include <stdio.h>

int main() {
int i,a,count=0,num[1000];
scanf("%d",&a);

if(0<=a && a<100)
	printf("%d",a);
else
{for(i=0;a!=0;i++)
{
	num[i]=a%1000;
	a=a/1000;
	count++;
}

printf("%d,",num[count-1]);
for(i=count-2;i>0;i--)
{if (0<=num[i] && num[i]<10)
  printf("00%d,",num[i]);
 
 else if(10<=num[i] && num[i]<100)
  printf("0%d,",num[i]);
 
 else printf("%d,",num[i]);
}
if (0<=num[0] && num[0]<10)
  printf("00%d",num[0]);
 
 else if(10<=num[0] && num[0]<100)
  printf("0%d",num[i]);
else
printf("%d",num[0]);}

return 0;
}
