import sys 
input = sys.stdin.readline

lenA, lenB = map(int,input().rstrip().split())
A, B = input().rstrip().split()

alpha = {
    "A":3, "B":2, "C":1, "D":2, "E":4, "F":3, "G":1, "H":3, "I":1, "J":1, 
    "K":3, "L":1, "M":3, "N":2, "O":1, "P":2, "Q":2, "R":2, "S":1, "T":2,
    "U":1, "V":1, "W":1, "X":2, "Y":2, "Z":1
}
mixWord = ''.join(a + b for a, b in zip(A, B)) + A[len(B):] + B[len(A):]
nums = [alpha[ch] for ch in mixWord]

while len(nums) > 2:
    new_nums = []
    for i in range(len(nums) - 1):
        new_nums.append((nums[i] + nums[i+1]) % 10)
    nums = new_nums

result = int(f"{nums[0]}{nums[1]}")  
print(f"{result}%")