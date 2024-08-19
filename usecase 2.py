# create a dictionary see if the input is hashable or not
# and reverse key to values and values to key
# here i have used to string to make unhasable values to key.

lt = [1, 2, 3, 4, 5, 6]
st = {1, 2, 34, 5, 6, 7}
tp = (12, 3, 4, 6)

int_var = 10
string = "key"
ft = 45.5

dt = {int_var: lt, string: st, tp: ft}
print("Inputted dictionary is :", dt)
res_dt = {}
for key, val in dt.items():
  try:
    res_dt[val] = key
  except:
    print("The not hashable value to key in dictionary is: ", val)
    res_dt[str(val)] = key
  else:
    res_dt[val] = key

print("Resultant dictionary is :", res_dt)
