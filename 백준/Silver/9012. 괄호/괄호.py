answer=[]
N=int(input())

for _ in range(N):
    
    toggle=0
    toggle_start=0
    VPS=input()

    for i in range(len(VPS)):
        
        if toggle<0:
            break
    
        if VPS[i]=='(':
            if toggle_start==0:
                toggle_start=1
                toggle+=1
            else:
                toggle+=1
        else:
            if toggle_start==1 and toggle==1:
                toggle_start=0
                toggle-=1
            else:
                toggle-=1
            
    if toggle==0 and toggle_start==0:
        answer.append("YES")
    else:
        answer.append("NO")

for row in answer:
    print(row)
   