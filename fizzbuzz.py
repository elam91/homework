

beforelist = list(range(1,101))
fizzbuzz1 = ["fizzbuzz" if x%3==0 and x%5==0  else x for x in beforelist]
fizzbuzz2 = ["fizz" if x!="fizzbuzz" and x%3==0 else x for x in fizzbuzz1]
fizzbuzz3 = ["buzz" if x!="fizzbuzz" and x!="fizz" and x%5==0 else x for x in fizzbuzz2]
print (fizzbuzz3)