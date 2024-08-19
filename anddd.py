# operator overloading using magic function. Converting the bitwise operator to logical operator.


class And:

  def __init__(self, a):
    self.a = a

  def __and__(self, other):

    if self.a == "False":
      return "False"

    elif other.a == "False":
      return "False"

    elif self.a == "True":
      if other.a == "True":
        return "True"

    elif self.a == "True":
      if other.a == "False":
        return "False"

    else:
      print("Pass only boolean values")


o1 = And("True")
o2 = And("True")
o3 = And("Val")
o4 = And("False")

print("True and True: ", o1 & o2)  # True
print("True and False: ",o1 & o4)  # False
print("False and True: ", o4 & o1)  # False
print("False and False: ", o4 & o4)  # False
print("Val and True", o3 & o2)  # Pass only boolean values