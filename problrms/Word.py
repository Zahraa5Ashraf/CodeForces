word= input("Enter word:")
countUp=0
countLow=0
for i in range(len(word)) :
     if word[i].isupper():
        countUp+=1
     else:
        countLow+=1
if countUp>countLow: print(word.upper()) 
else: print(word.lower())
         


