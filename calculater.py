
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
dic={"+":add,"-":sub,"*":mul,"/":div}

num1=int(input("enter first num: "))
a=True
while a:
    
    print("+,-,*,/")
    num2=input("select one operators: ")
    num3=int(input("enter second num: "))

    cal=dic[num2]
    ans=cal(num1,num3)
    print(f"{num1} {num2} {num3}= {ans}")
    
    if input("want to coninue press 'y' or for not press 'n' ")=="y":
        num1=ans

    else:
        a=False

    
