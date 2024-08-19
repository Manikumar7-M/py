records = ["a","b", "c", "d", "e", "f"]
rec = input("Enter the input: ")

for x in records:
    if rec == x:
        break
else:
    records.append(rec)
print(records)