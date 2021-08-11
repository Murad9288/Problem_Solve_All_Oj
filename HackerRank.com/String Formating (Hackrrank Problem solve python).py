# Eikhane 3ti code diye ekoi kaj korano hoyeche..
def print_formatted(number):
     results = []
     for i in range(1,n+1):
          d = str(i)
          o = str(oct(i)[2:])
          h = str(hex(i)[2:]).upper()
          b = str(bin(i)[2:])
          results.append([d,o,h,b])
     width = len(results[-1][3])
     for i in results:
          print(*(rep.rjust(width) for rep in i))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
# Ek line a code nirnoy...    
    '''n = int(input())
[print(*[s.rjust(len(bin(n)[2:])) for s in [str(i),oct(i)[2:],hex(i).upper()[2:],bin(i)[2:]]]) for i in range(1,n+1)]'''


# Eikhane Function chara korano hoyeche..
'''n = int(input())
results = []
for i in range(1,n+1):
     d = str(i)
     o = str(oct(i)[2:])
     h = str(hex(i)[2:]).upper()
     b = str(bin(i)[2:])
     results.append([d,o,h,b])
width = len(results[-1][3])
for i in results:
     print(*(rep.rjust(width) for rep in i))'''
