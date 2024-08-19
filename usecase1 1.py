# find duplicate character in list

a = [1,2,2,3,3,4,5]
b = "asdasdasdasdasdasdasdasdasdasdasdas"

a_set = set(a)
b_set = set(b)

res = []
res_str = []

for i in a_set:
  if a.count(i) > 1:
    res.append(i)
    
for j in b_set:
  if b.count(j) > 1:
    res_str.append(j)

res_set = list(set(res))
res_set = list(set(res))

print(res)
print(''.join(res_str))