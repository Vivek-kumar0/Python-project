
fruits=["apple","banana","grapes","cherry","strawberry","pomegranate","coconut","guava","papaya"]
import random

randomWord=random.choice(fruits)

emp=[]

for i in range(len(randomWord)):
    emp+="_"

end=False
while not end:
    user=input("Enter a letter : ").lower()


    for l in range(len(randomWord)):
        letter=randomWord[l]
        

        if (letter==user):
            emp[l]=letter

    print(emp)

    if "_" not in emp:
        end=True

        print("you win")
    
    

    
    
   

    
