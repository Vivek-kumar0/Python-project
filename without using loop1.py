def printno(uppe):
    if(uppe>0):
        printno(uppe-1)
        print(uppe)
uppe=int(input("Enter upper limit: "))
printno(uppe)
