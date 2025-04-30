def solution(n: int) -> int:
    return n + sum(map(int, str(n)))

arr=set()
for num in range(1, 10001):
    arr.add(solution(num))

for num in range(1, 10001):
    if num not in arr:
        print(num)
    