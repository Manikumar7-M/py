# emp_name, emp_id, salary, place, dept

# create a dict to accept amny thigs
details = {}

def take_input():
    emp_name = input("Enter the Employee name: ")
    emp_id= int(input("Enter the Employee ID: "))
    emp_salary = int(input("Enter the Employee salary: "))
    emp_place = input("Enter the Employee Place: ")
    emp_dept  = input("Enter the Employee details: ")
    return emp_details(emp_name, emp_id, emp_salary, emp_place, emp_dept)

def emp_details(*emp):
    details[emp[1]] = {"emp_name": emp[0], "emp_id":emp[1], "emp_salary":emp[2], "emp_place":emp[3], "emp_dept":emp[4]}
    return details


a = 0
while(a != -1):
    print("Enter -1 to exit")
    a = int(input("Enter 0 to enter details"))
    if a == 0:
        res = take_input()
        print(res)