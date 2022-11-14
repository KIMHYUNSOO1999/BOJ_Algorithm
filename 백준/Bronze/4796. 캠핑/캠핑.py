import sys
input=sys.stdin.readline

CNT = 1

while True:
  result = 0
  L, P, V = map(int, input().split())
  
  if L + P + V == 0:
    break
  
  result = ((V//P) * L) + min((V%P), L)
    
  print(f"Case {CNT}: {result}")
  CNT += 1
