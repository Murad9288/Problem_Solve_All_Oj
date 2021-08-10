X = float(input())
Y = X
A = Y/100
B = Y%100
C = B/50
D = B%50
E = D/20
F = D%20
G = F/10
H = F%10
I = H/5
J = H%5
K = J/2
L = J%2
M = X*100
N = int(M)
O = N%100
P = O/50
Q = O%50
R = Q/25
S = Q%25
T = S/10
U = S%10
V = U/5
W = U%5
print("NOTAS:")
print("%d nota(s) de R$ 100.00"%(int(A)))
print("%d nota(s) de R$ 50.00"%(int(C)))
print("%d nota(s) de R$ 20.00"%(int(E)))
print("%d nota(s) de R$ 10.00"%(int(G)))
print("%d nota(s) de R$ 5.00"%(int(I)))
print("%d nota(s) de R$ 2.00"%(int(K)))
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00"%(int(L)))
print("%d moeda(s) de R$ 0.50"%(int(P)))
print("%d moeda(s) de R$ 0.25"%(int(R)))
print("%d moeda(s) de R$ 0.10"%(int(T)))
print("%d moeda(s) de R$ 0.05"%(int(V)))
print("%d moeda(s) de R$ 0.01"%(int(W)))
