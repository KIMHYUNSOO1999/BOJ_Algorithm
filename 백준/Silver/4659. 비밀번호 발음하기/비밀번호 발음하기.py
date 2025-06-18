import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()

    if s == 'end':
        break
        
    flag = [0,1,1]
    flag_l=0
    flag_r=0
    w = 'aeiou'
    w2='eo'

    for i in range(len(s)):
        
        if s[i] in w:
            flag[0] = 1
            flag_l += 1
            flag_r = 0
        else:
            flag_l = 0
            flag_r +=1
    
        if flag_l == 3 or flag_r == 3:
            flag[1]=0
    
        if i!=0 and s[i] not in w2 and s[i] == s[i-1]:
            flag[2]=0

    
    
    if sum(flag)==3:
        print(f'<{s}> is acceptable.')
    else:
        print(f'<{s}> is not acceptable.')