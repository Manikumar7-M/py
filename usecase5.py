# Bridegroom and bride matching taking both the details and matching.

# radha = {
#     "Height": 5.5,
#     "Age": 23
# }

# lakshmi = {
#     "Height": 5,
#     "Age": 25
# }
# girls = {
#     "Radha":
#     {
#         "Height": 5.5,
#         "Age": 23,
#         "Req_in_boi":
#         {
#             "Height": 5.7,
#             "Age": 28, 
#         }
#     },
#     "Radha":
#     {
#         "Height": 5.5,
#         "Age": 23,
#         "Req_in_boi":
#         {
#             "Height": 5.7,
#             "Age": 28, 
#         }
#     }
# }
girls = dict()
boi = dict()

what_to_do = -2
while(what_to_do != -1):

    print("Enter 0: Provide Boi details")
    print("Enter 2: Provide Girl details")
    print("Enter 1: Get Records for Boi")
    print("Enter 3: Get Records for Girl")
    
    print("Enter -1 to Exit")
    what_to_do = int(input())
    
    if what_to_do == 0:
        boi_name = input("Enter your name (BOI): ")
        boi_height = float(input("Enter the Height (BOI):"))
        boi_edu = input("Enter the education details (BOI): ")
        boi_salary = int(input("Enter the salary (BOI): "))
        boi_company = input("Enter the company (BOI): ")
        boi_age = int(input("Enter the age (BOI): "))

        boi_list = {"boi_actual_name": boi_name, "boi_height":boi_height, "boi_edu":boi_edu, "boi_salary":boi_salary, "boi_company":boi_company, "boi_age":boi_age}

        boi[boi_name] = boi_list
        boi[boi_name]['Status'] = []

        for girl_name in girls:
            if(boi[boi_name]["boi_height"] == girls[girl_name]["Req_in_boi_by_girl"]["req_girl_height"]) and (girls[girl_name]["Req_in_boi_by_girl"]["req_girl_edu"] in boi[boi_name]["boi_edu"]) and (boi[boi_name]["boi_salary"] >= girls[girl_name]["Req_in_boi_by_girl"]["req_girl_salary"]) and (boi[boi_name]["boi_company"] == girls[girl_name]["Req_in_boi_by_girl"]["req_girl_company"]) and (boi[boi_name]["boi_age"] == girls[girl_name]["Req_in_boi_by_girl"]["req_girl_age"]):
                # print(girls)
                print("Paired with"+" "+girls[girl_name]["girl_actual_name"]+ " "+"profile.")
                boi[boi_name]["Status"].append("Paired with"+" "+girls[girl_name]["girl_actual_name"]+ " "+"profile.")
                print(" ")
            else:
                print("Not matched with no one")
                boi[boi_name]["Status"] = "Reject with all girls"
                print(" ")

    elif what_to_do == 1:
        print("BOI'S PROFILE: ",boi)
    elif what_to_do == 2:
        girl_name = input("Enter your name (GIRL): ")
        girl_height = float(input("Enter the Height (GIRL):"))
        girl_age = int(input("Enter the age (GIRL): "))

        print("---------ENTER BOI REQUIREMENT DETAILS---------")
        req_girl_edu = input("Enter the education details of boi that required by the girl: ")
        req_girl_salary = int(input("Enter the salary of boi that required by the girl: "))
        req_girl_company = input("Enter the company of boi that required by the girl: ")
        req_girl_height = float(input("Enter the Height of boi that required by the girl:"))
        req_girl_age = int(input("Enter the age of boi that required by the girl: "))

        girl_list = {
            "girl_actual_name": girl_name, 
            "girl_height":girl_height, 
            "girl_age":girl_age, 
            "Req_in_boi_by_girl":{
                "req_girl_edu":req_girl_edu,
                "req_girl_salary":req_girl_salary,
                "req_girl_company": req_girl_company,
                "req_girl_height": req_girl_height,
                "req_girl_age": req_girl_age
            }
        }
        # boi.update(dict(zip("Boi"+str(count), boi_list)))
        girls[girl_name] = girl_list

    elif what_to_do == 3:
        print("GIRLS'S PROFILE: ",girls)

        
    # else:
    #     print("Enter the correct number")
        

    
