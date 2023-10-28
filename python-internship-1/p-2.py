import time
password=3340
i=5
while(i>=0):
    password=str(input("Enter the password"))
    i=i-1
    if(password=="3340"):
        print("Access granted")
        break
    elif(i==0):
        print("chances over........try again after 5 seconds")
        count=5
        while(count>0):
            print(count)
            time.sleep(1)
            count=count-1
        i=5
    else:
        print("number of remaining chances",i)
        
        
        
    
    
    
