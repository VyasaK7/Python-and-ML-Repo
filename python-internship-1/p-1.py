weight=float(input('Enter your weight:'))
unit=input("P or K")
if unit.upper=='P':
    c=weight/2
    print(c)
elif unit.upper()=='K':
    c=weight*2
    print(c)
else:
    print("Invalid")
    
