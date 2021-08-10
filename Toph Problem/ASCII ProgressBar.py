f_n = int(float(input()))
n = f_n//10
plus_sign = '+'*n
dot_sign = '.'*(10-n)
percent = f_n
print('[{}{}] {}%'.format(plus_sign,dot_sign,percent))
