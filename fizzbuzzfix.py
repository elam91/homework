def fizzorbuzz(a):
    if(a%3 == 0):
        if(a % 5 == 0): 
            a= "fizzbuzz"
        else:
            a= "fizz"
    elif(a%5 == 0):
         a= "buzz"
    return a

mylist = list(range(1,101))
fizzbuzz1 = [fizzorbuzz(x) for x in mylist]

print (fizzbuzz1)