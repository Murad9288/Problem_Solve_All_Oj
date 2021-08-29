for T in range(int(input())):
    r1,r2,B = map(int,input().split())
    jotobol_khelse = 300-B
    current_run_rate = r2/(jotobol_khelse/6)
    target = r1+1
    required_run_rate = (target-r2)/(B/6)
    if r2>r1:
        required_run_rate = 0.00
    print("%.2f %.2f"%(current_run_rate,required_run_rate))
