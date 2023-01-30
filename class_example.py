class People:
  def __init__(self, age, name):
    self.age = age
    self.name =  name
  def isAdult(self):
    return self.age >= 18

lazp = People(15, "Lazp")
print(lazp.name)
print(lazp.isAdult())