# Bridegroom application

radha = {
    "Height": 5.5,
    "Age": 23
}

lakshmi = {
    "Height": 5,
    "Age": 25
}
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

boi = dict()
count = 0
what_to_do = -2
while(what_to_do != -1):

    print("Enter 0: Provide Groom details")
    print("Enter 1: Get Records")
    print("Enter -1 to Exit")
    what_to_do = int(input())
    
    if what_to_do == 0:
        boi_name = input("Enter your name: ")
        boi_height = float(input("Enter the Height:"))
        boi_edu = input("Enter the education details: ")
        boi_salary = int(input("Enter the salary: "))
        boi_company = input("Enter the company: ")
        boi_age = int(input("Enter the age: "))
        count += 1

        boi_list = {"boi_actual_name": boi_name, "boi_height":boi_height, "boi_edu":boi_edu, "boi_salary":boi_salary, "boi_company":boi_company, "boi_age":boi_age}
        # boi.update(dict(zip("Boi"+str(count), boi_list)))
        boi[boi_name] = boi_list

        if(boi[boi_name]["boi_height"] > radha['Height']) and ("master degree" in boi[boi_name]["boi_edu"]) and (boi[boi_name]["boi_salary"] >= 1000000) and (boi[boi_name]["boi_company"] == "MNC") and ((boi[boi_name]["boi_age"] == radha['Age']) or (boi[boi_name]["boi_age"] == (radha['Age']+5))):
            print("Matched with Radha's Profile")
            boi[boi_name]["Status"] = "Paired with Radha's profile"
        elif(boi[boi_name]["boi_height"] >= lakshmi['Height']) and ("degree" in boi[boi_name]["boi_edu"]) and (boi[boi_name]["boi_salary"] >= 2000000) and ((boi[boi_name]["boi_age"] == lakshmi['Age']) or (boi[boi_name]["boi_age"] == (lakshmi['Age']+2))):
            print("Matched with Lakshmi's Profile")
            boi[boi_name]["Status"] = "Paired with Laksmi's profile"
        else:
            print("Not matched with no one")
            boi[boi_name]["Status"] = "Reject with all girls"
    elif what_to_do == 1:
        print("BOI'S PROFILE: ",boi)
    # else:
    #     print("Enter the correct number")
        

    
