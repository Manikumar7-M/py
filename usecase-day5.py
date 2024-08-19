student_records = {}

def accept_input():
    student_id = int(input("Enter the student id: "))
    student_name = input("Enter the name: ")
    college_name = input("Enter the college name: ")
    marks = input("Enter the marks for 6 subject: ").split(" ")
    return student_name, student_id, college_name, marks

def make_nested_dict_info(name, college, marks):
    a = dict()
    a["name"] = name
    a["college"] = college
    a["marks"] = marks # string of marks
    return a

def store_data(id, nested_dict_info):
    global student_records
    student_records[id] = nested_dict_info
    sum_val = 0
    for mark in student_records[id]['marks']:
        sum_val += int(mark)
    sum_val = (sum_val/6)*100
    student_records[id]['percentage'] = int(sum_val)
    return student_records

def print_dict(d):
    print(d)

def ask():
    print()
    print("*****************************************************************")
    print("*                    Enter -1 to exit                           *")
    print("*                Enter 1 to students records                    *")
    print("*        Enter 2 to search for student records                  *")
    print("*        Enter 3 to search for student college                  *") # student name should be displayed of a college input is college
    print("*        Enter 4 to display who is the topper in the college    *")
    print("*    Enter 5 display all the records (specified college or all) *") # All the details should be displayed of a college input is college name
    print("*****************************************************************")
    print()
    

def serach_students(student_id):
    if student_id in student_records:
        print(f"--------------Student Details for {student_id}--------------")
        print(student_records[student_id])
    else:
        print("Student NOT found in the records")

def search_for_student_college(student_id):
    if student_id in student_records:
        print(f"------------------Student College for {student_id}------------------")
        print(f'{student_id}\'s college is {student_records[student_id]["college"]}')
    else:
        print("Student NOT found in the records")

def search_topper():
    max_val = 0
    for id in student_records:
        if student_records[id]['percentage'] > max_val:
            max_val, name = student_records[id]['percentage'], student_records[id]['name']
    return max_val, name



what_to_do = 0
while(what_to_do != -1):
    
    ask()
    what_to_do = int(input("Enter your choice >>> "))

    if(what_to_do == 1):
        name, id, college, marks = accept_input()
        info = make_nested_dict_info(name, college, marks)
        store_data(id, info)
    elif(what_to_do == 2):
        search_student_id = int(input("Enter the student ID: "))
        serach_students(search_student_id)
    elif(what_to_do == 3):
        search_student_id_college = int(input("Enter the student ID: "))
        search_for_student_college(search_student_id_college)
    elif(what_to_do == 4):
        score, name = search_topper()
        print(f"------------------Topper------------------")
        print(f'{name} is the topper has scored {score}')
    elif(what_to_do == 5):
        print_dict(student_records)
