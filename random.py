word=["apple","orange","papaya","grapes"]

import random

rndWrd=random.choice(word)

print(rndWrd)
emp=[]

for i in range(len(rndWrd)):
    emp+="_"
print(emp)

end=False

while not end:
    userWord=input("Enter a letter: ").lower()

    for pos in range(len(rndWrd)):
        letter=rndWrd[pos]
        
        if (letter==userWord):
            emp[pos]=letter
    print(emp)
            
    if "_" not in emp:
        end=True

        print("You Win")


    
