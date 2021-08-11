# Function chara korano hoyeche..
'''import textwrap
s = input()
w = int(input())
l = " ".join(textwrap.wrap(s,w))
print(textwrap.fill(l,w))'''

# niche Function diye korano hoyeche....

import textwrap
def wrap(string, max_width):
   m = " ".join(textwrap.wrap(string,max_width))
   L = textwrap.fill(string,max_width)
   return L
if __name__ == '__main__':
    string = input()
    max_width = int(input())
    result = wrap(string, max_width)
    print(result)

    

