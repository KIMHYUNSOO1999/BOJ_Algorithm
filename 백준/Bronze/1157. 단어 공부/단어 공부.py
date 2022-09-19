N=input().upper()
N_list = list(set(N))

cnt = []
for i in N_list:
  count = N.count
  cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
  print("?")

else:
  print(N_list[(cnt.index(max(cnt)))])