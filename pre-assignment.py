# take a input validate if ph no. or not

mobile = input("Enter the mobile number: ")

if len(mobile) == 10 and mobile.isdecimal() and (mobile.startswith("6") or mobile.startswith("7") or mobile.startswith("8") or mobile.startswith("9")):
    print("Valid mobile number")
else:
    print("Invalid Mobile number")