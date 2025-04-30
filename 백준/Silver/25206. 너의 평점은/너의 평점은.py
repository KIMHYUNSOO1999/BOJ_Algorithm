import sys
input = sys.stdin.readline

grade = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

num = 0
den = 0
for _ in range(20):
    a, b = input().rstrip().split()[1:]

    if b != 'P':
        num += (float(a) * grade[b])
        den += float(a)

print(round(num/den,6))