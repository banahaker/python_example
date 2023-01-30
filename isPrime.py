# IsPrime Problem Solve (While Loop Method)

def isPrime(n):
  c = 2
  while c <= n:
    if n%c == 0:
      return True
      c+=1

  return False

print(isPrime(123456))