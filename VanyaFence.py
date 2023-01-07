# user enter values
n= int(input("text")) 
h= int(input("text"))
#enter from user into list
friends= list(map(int, input("text").split()))
w=0  #define width variable
for i in friends:
	if i>h : w+=2
	else: w+=1
print(w)
