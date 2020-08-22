def fizzorbuzz(num: int):
    if(num % 3 == 0):
        if(num % 5 == 0):
            num = "fizzbuzz"
        else:
            num = "fizz"
    elif(num % 5 == 0):
        num = "buzz"
    return num


num_list = list(range(1, 101))
fizzbuzz1 = [fizzorbuzz(x) for x in num_list]

print(fizzbuzz1)
