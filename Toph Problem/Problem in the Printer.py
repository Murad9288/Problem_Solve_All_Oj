# Python Code:

while True:
    s = str(input()).lower()
    s2 = ""
    for i in range(len(s)):
        if s[i] == "6":
            s2 += "b"
        elif s[i] == "9":
            s2 += "g"
        elif s[i] == "1":
            s2 += "l"
        elif s[i] == "0":
            s2 += "o"
        elif s[i] == "5":
            s2 += "s"
        elif s[i] == "2":
            s2 += "z"
        elif s[i] == "b":
            s2 += "6"
        elif s[i] == "g":
            s2 += "9"
        elif s[i] == "l":
            s2 += "1"
        elif s[i] == "o":
            s2 += "0"
        elif s[i] == "s":
            s2 += "5"
        elif s[i] == "z":
            s2 += "2"
        else:
            s2 += s[i]
    if s == "the end.":
        break
    else:
        print(s2)

# C++ Code:

'''
#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s,stop="the end.";
    for(;getline(cin,s);)
    {
        if(s==stop)
            break;
        for(int i=0; s[i]!='\0'; i++){
            if(s[i]=='6')
                s[i]='b';
            else if(s[i]=='9')
                s[i]='g';
            else if(s[i]=='1')
                s[i]='l';
            else if(s[i]=='0')
                s[i]='o';
            else if(s[i]=='5')
                s[i]='s';
            else if(s[i]=='2')
                s[i]='z';
            //letters to numbers
            else if(s[i]=='b')
                s[i]='6';
            else if(s[i]=='g')
                s[i]='9';
            else if(s[i]=='l')
                s[i]='1';
            else if(s[i]=='o')
                s[i]='0';
            else if(s[i]=='s')
                s[i]='5';
            else if(s[i]=='z')
                s[i]='2';
        }
        cout<<s<<endl;
    }
    return 0;
}

'''
