# Example for GCD function

def GCD(x, y):
  if x > y :
    c = x
  else:
      c = y
  for k in range(c, 2, -1):
      if x % k == 0 and y % k == 0:
          return k
  return 1

print(GCD(5, 3))