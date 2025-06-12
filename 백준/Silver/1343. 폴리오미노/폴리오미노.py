import sys
input = sys.stdin.readline

board = input().rstrip()

result = []

cnt = 0
for i in range(len(board)):
         
    if board[i] == 'X':
        cnt +=1
    else:
        result.append('.')
        cnt = 0

    if cnt == 4:
        cnt = 0
        result.append('AAAA')

    if i<len(board)-1 and board[i+1]!='X' and cnt == 2:
        cnt = 0
        result.append('BB')
    elif i==len(board)-1 and cnt == 2:
        cnt = 0
        result.append('BB')

answer = ''.join(result)

if len(answer) != len(board):
    print(-1)
else:
    print(answer)
