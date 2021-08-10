a,b,c,d = map(float,input().split())
#Formurla unujayi..
result_1 = (a*2+b*3+c*4+d*1)/10
print("Media: %0.1f"%result_1)
if result_1 >= 7.0:
    print("Aluno aprovado.")
elif result_1 < 5.0:
    print("Aluno reprovado.")
elif result_1 >= 5.0 and result_1 <= 6.9:
    print("Aluno em exame.")
    n = float(input())
    print("Nota do exame: %0.1f"%n)
    result_2 = (result_1+n)/2
    if result_2 >= 5.0:
        print("Aluno aprovado.")
        print("Media final: %0.1f"%result_2)
    else:
        print("Aluno reprovado.")
        print("Media final: %0.1f"%result_2)
