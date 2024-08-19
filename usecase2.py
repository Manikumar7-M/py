# take two parameter and compare using oops

class X:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def compare(self):
    if self.x > self.y:
      print(f"{self.x} is greater than {self.y}")
    else:
      print(f"{self.y} is greater than {self.x}")

  def __gt__(self):
    print("I am in Greater")
    return True
    

obj = X(10, 20)
# obj.compare()
if obj.x > obj.y:
  print(f"{obj.x} is greater than {obj.y}")
