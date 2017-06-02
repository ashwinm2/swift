def check(temp):
  root = int(temp ** 0.5)
  if temp % 2 == 0:
    return False
  else:
    if root % 2 == 0:
      root -= 1
    
    while root > 1:
      if temp % root == 0:
        return False
      root -= 2
    return True

def F(n):
  first = 0
  print "BuzzFizz"
  second = 1
  print "BuzzFizz"
  while n > 0:
    temp = first + second
    if check(temp):
      print "BuzzFizz"
    else:
      if temp % 15 == 0:
        print "FizzBuzz"
      elif temp % 5 == 0:
        print "Fizz"
      elif temp % 3 == 0:
        print "Buzz"
      else:
        print temp
    first = second
    second = temp
    n-= 1


F(15)