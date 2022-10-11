N=int(input())

people=[]
for _ in range(N):
    age,name=map(str,input().split())
    people.append((int(age),name))
      
people.sort(key = lambda x : int(x[0]))

for row in people:
    print(row[0],row[1])