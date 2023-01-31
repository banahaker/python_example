def GCD(x, y):
  if x > y :
    c = x
  else:
      c = y
  for k in range(c, 2, -1):
      if x % k == 0 and y % k == 0:
          return k
  return 1

def isPrime(n):
  c = 2
  while c < n:
    if n%c == 0:
      return True
    c+=1

  return False

def lazpPleaseYou(cupA, cupB):
  if cupA >= cupB:
    return cupA
  return cupB