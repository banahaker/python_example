# Example for decorator

def print_func(func):
  def wrap():
    print("The function is " + func.__name__)
    func()
  return wrap

@print_func
def a():
  print("aaa")

@print_func
def b():
  print("bbb")

if __name__ == "__main__":
  a()
  b()