# user enter values
n= int(input("Enter number of friends")) 
h= int(input("Enter Height of fence"))
#enter from user into list
friends= list(map(int, input("Enter heights of friends").split()))
w=0  #define width variable
for i in friends:
	if i>h : w+=2
	else: w+=1
print(w)
