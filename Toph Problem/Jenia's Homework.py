import math
for _ in range(int(input())):
    n = int(input())
    area = math.sqrt(n)/2.0
    spa = math.pi*area*area
    print("%.10f %.10f"%(n-spa,2*math.pi*area))
