A = int(input())
binary = str(bin(A))
bi_li = binary[2:]
rep = bi_li.replace("0","")
res = int(rep,2)
print(res)
