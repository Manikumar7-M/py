# take input store it in dict

# student name, id, branch, dept, clg, marks

# name = input("Enter the name: ")
# id = int(input("Enter the id: "))
# branch = input("Enter the branch: ")
# dept = input("Enter the Dept: ")
# clg = input("Enter the Clg: ")
# marks = input("Enter the marks: ").split(" ")

# list_default = ["Names", "ID", "Branch", "Department", "College", "Marks"]
# list_values = [name, id, branch, dept, clg, marks]

# d = {id:[name, branch, dept, clg, marks]}
# details = {
#     "Name":name,
#     "ID": id,
#     "Branch" : branch,
#     "College": clg,
#     "Marks": marks
# }

# details_zip = dict(zip(list_default, list_values))
# print(d)
# print(details)
# print(details_zip)
import time
import sys

flag = 0
details_zip = dict()
while (1):
    i = input("Want to add details?: ")
    
    # time.sleep(i)
    sys.stdout.flush()
    print()

    if i == "Y":
        # print("ASD")
        flag +=1
    elif i == "N":
        flag = 1
        break
    else:
        print("Please enter Y or N")
        continue

    # flag+=1

    name = input("Enter the name: ")
    id = int(input("Enter the id: "))
    branch = input("Enter the branch: ")
    dept = input("Enter the Dept: ")
    clg = input("Enter the Clg: ")
    marks = input("Enter the marks: ").split(" ")

    list_default = ["Names"+str(flag), "ID"+str(flag), "Branch"+str(flag), "Department"+str(flag), "College"+str(flag), "Marks"+str(flag)]
    list_values = [name, id, branch, dept, clg, marks]

    details_zip.update(zip(list_default, list_values))

print(details_zip)