'''size = int(input())
alpha = "abcdefghijklmnopqrstuvwxyz"
subset = alpha[:size]
base = "-".join(reversed(subset))
rows = []
for i in range(size):
     row = base[:len(base) - i*2]
     row = ("-" * (len(base) - len(row))) + row
     rows.insert(0, row)
rows.extend(reversed(rows[:-1]))
for i in range(len(rows)):
     row = rows[i]
     rev_row = row[::-1]
     rows[i] = row + rev_row[1:] 
print(*rows, sep="\n")'''

# Function diye korano hoyeche...
def print_rangoli(size):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(size-1,-size,-1):
        temp = '-'.join(alp[size-1:abs(i):-1]+alp[abs(i):size])
        print(temp.center(4*size-3,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
