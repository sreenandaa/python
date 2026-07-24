for i in range(1,101):
    if(i%3==0 and i%5==0):
        print(i,"FizzBuzz",sep="==")
    elif(i%3==0):
        print(i,"Fizz",sep="==")
    elif(i%5==0):
        print(i,"Buzz",sep="==")
    else:
        print(i)

