n= int(input("Enter number of games played"))
s= input("Enter initial of each winner") #for string array
anton=0
danik=0
w= ""
for i in s:
	if i =="A" : anton+=1
	if i =="D" : danik+=1
	
if anton>danik:
    w ="Anton"
elif danik>anton:
    w = "Danik"
else:
    w = "friendship"
print(w)
 