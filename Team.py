n= int(input("enter number of problems"))
i=0
problem=0
while i<n:
    count=0
    t=list(map(int,input("enter the predictions between 0,1").split()))
    for j in t:
        if j==1: count+=1
    if count>=2: problem+=1
    
    i+=1

print(problem)
    
    