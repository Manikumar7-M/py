# pateient name, age, 
# Menu
# Accept patient records, use generator to generate patient id
# HOSPITAL MANAGEMENT

patient_records = {}
doctor_records = {
    "General":{
        "1":{
            "Doctor_name": "Gen A",
            "Status": "Free"
        },
        "2":{
            "Doctor_name": "Gen B",
            "Status": "Free",
        },
        "3":{
            "Doctor_name": "Gen C",
            "Status": "Free",
        },
        "4":{
            "Doctor_name": "Gen D",
            "Status": "Free",
        }
    },
    "Higher Level":{
        "1":{
            "Doctor_name": "Gen HL A",
            "Status": "Free"
        },
        "2":{
            "Doctor_name": "Gen HL B",
            "Status": "Free",
        },
        "3":{
            "Doctor_name": "Gen HL C",
            "Status": "Free",
        },
        "4":{
            "Doctor_name": "Gen HL D",
            "Status": "Free",
        }
    }
}

def get_id():
    # for i in range(x):
    #     yield i 
    yield from range(1000,2000)
id = get_id()



def ask():
    print("-------------------------------------")
    print("1. Front Desk") # accept patient records => name, age, problem and assign the doctor based on the problem
    print("2. Doctor") # display all the patient name waiting for doctor
    print("3. Lab") 
    print("4. Finance")
    print("5. Display all records")
    print("6. Prescribe")
    print("-1. To exit")
    print("-------------------------------------")
    option = int(input("Enter: "))
    return option

def accept_details_and_assign():
    global patient_records
    patient_name = input("Enter the patient name: ")
    patient_age = int(input("Enter the patient age: "))
    patient_problem = input("Enter the patient problem: ")
    patient_place = input("Enter the patient place: ")
    patient_id = next(id)
    patient_records[patient_id] = {"Name": patient_name, "Age": patient_age, "Problem":patient_problem, "Place":patient_place, "Status": "Waiting for doctor"}

    print(patient_records[patient_id]["Status"])

    if "fever" in patient_problem or "cold" in patient_problem or "chills" in patient_problem:
        patient_records[patient_id]["Status"] = "Assigned to General Doctor"
        print(patient_records[patient_id]["Status"])
        for i in doctor_records["General"]:
            if doctor_records["General"][i]["Status"] == "Free":
                patient_records[patient_id]["Status"] = f'Assigned to {i} id and {doctor_records["General"][i]["Doctor_name"]}.'
                doctor_records["General"][i]["Status"] = f'Took {patient_records[patient_id]["Name"]}'
                print(patient_records[patient_id]["Status"])
                break
        else:
            print("None of the doctor is Free")

    elif "Cancer" in patient_problem or "Heart issue" in patient_problem or "Die" in patient_problem:
        patient_records[patient_id]["Status"] = "Assigned to Higher Level Doctor"
        if 'Heart issue' in patient_records[patient_id]["Problem"]:
            print("Higher level doctor send to lab for mri scan")
            patient_records[patient_id]["Status"] = "Waiting for Lab"
            print(patient_records[patient_id]["Status"])
            
        print(patient_records[patient_id]["Status"])
        for i in doctor_records["Higher Level"]:
            if doctor_records["Higher Level"][i]["Status"] == "Free" and "Heart issue" not in patient_problem:
                patient_records[patient_id]["Status"] = f'Assigned to {i} id and {doctor_records["Higher Level"][i]["Doctor_name"]}.'
                doctor_records["Higher Level"][i]["Status"] = f'Took {patient_records[patient_id]["Name"]}'
                print(patient_records[patient_id]["Status"])
                break
        else:
            print("None of the doctor is Free")
         

def print_patient_waiting_for_doctor():
    for key in patient_records:
        if patient_records[key]["Status"] == "Waiting for doctor":
            print(patient_records[key])
    
def print_patient_waiting_for_lab():
    for key in patient_records:
        if patient_records[key]["Status"] == "Waiting for Lab":
            print(patient_records[key])
            patient_records[key]["Status"] = "Scan is done"
            print(patient_records[key]["Status"])
            patient_records[key]["Status"] = "Waiting for finance"
            print(patient_records[key]["Status"])

def print_patient_waiting_for_fin():
    for key in patient_records:
        if patient_records[key]["Status"] == "Waiting for finance":
            print(patient_records[key])
            patient_records[key]["Status"] = "finance is done"
            print(patient_records[key]["Status"])
            patient_records[key]["Done"] = "YES"

def presecribe():
    for key in patient_records:
        if "Assigned to" in patient_records[key]["Status"]:
            print(patient_records[key])
            if patient_records[key]["Problem"] == "cold":
                patient_records[key]["Presecription"] = "TABLET 1"
                patient_records[key]["Status"] = "Waiting for finance"
            elif patient_records[key]["Problem"] == "chills":
                patient_records[key]["Presecription"] = "TABLET 2"
                patient_records[key]["Status"] = "Waiting for finance"
            elif patient_records[key]["Problem"] == "fever":
                patient_records[key]["Presecription"] = "TABLET 3"
                patient_records[key]["Status"] = "Waiting for finance"
            
            print(patient_records[key]["Status"])
            print_patient_waiting_for_fin()

def display_all_records():
    print(patient_records)


what_to_do = 0

while (what_to_do != -1):

    what_to_do = ask()

    if what_to_do == 1:
        accept_details_and_assign()
    elif what_to_do == 2:
        # id, type = input("Enter the doctor id and type of doctor: ")
        # print_patient_waiting_for_doctor(int(id), type)
        print_patient_waiting_for_doctor()
    elif what_to_do == 3:
        print_patient_waiting_for_lab()
    elif what_to_do == 4:
        print_patient_waiting_for_fin()
    elif what_to_do == 5:
        display_all_records()
    elif what_to_do == 6:
        presecribe()
