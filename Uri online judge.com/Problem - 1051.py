tax = float(input())

if(tax > 0 and tax <= 2000):
 print("Isento")
elif(tax > 2000 and tax <= 3000):
 resto = tax - 2000
 resultado = resto * 0.08
 print("R$ %0.2f"%resultado)
elif(tax > 3000 and tax < 4500):
 resto = tax - 3000
 resultado = (resto * 0.18) + (1000 * 0.08)
 print("R$ %0.2f"%resultado)
else:
 resto = tax - 4500
 resultado = (resto * 0.28) + (1500 * 0.18) + (1000 * 0.08)
 print("R$ %0.2f"%resultado)
