p=int(input("enter principle amount\n"))
r=float(input("enter rate\n"))
t=float(input("enter time in year\n"))
ci=p*(1+r/100)**t
print("compound interest:",ci)
        
