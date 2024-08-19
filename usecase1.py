name = input("Enter the name: ")
marks = int(input("Enter the marks: "))

print("Failed") if(marks < 35) else (print("Passed") if(marks>35) else print("Failed"))