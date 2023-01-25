A,B = list(map(int,input().split()))
Result = lambda A,B: ">" if A>B else ("<" if A<B else "==")

print(Result(A,B))