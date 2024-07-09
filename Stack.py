stack=[]

def push():
    v=int(input("Enter a number to add: "))
    stack.append(v)
    print(stack)

def pop1():
    
    
    if not stack:
        print("stack is empty")

    else:
        stack.pop()
        print(stack)

while True:

    choice=int(input())
    if choice==1:
        push()

    elif choice==2:
        pop1()
        
    elif choice==3:
        break
    
    else:
        print("enter the correct")
        
        
