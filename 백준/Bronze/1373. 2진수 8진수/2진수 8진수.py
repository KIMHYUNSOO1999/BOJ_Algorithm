import sys
input=sys.stdin.readline 

CNT=0
CNT_row=0
Binary_8=""
result=""

Binary_2=input().rstrip()

for row in Binary_2[::-1]:
    
    Binary_8=row+Binary_8
    CNT_row+=1
    CNT+=1
    
    if CNT==3:
        result=str(int(Binary_8[0])*4+int(Binary_8[1])*2+int(Binary_8[2])*1)+result
        Binary_8=""
        CNT=0
        
    elif CNT_row==len(Binary_2):
        
        if len(Binary_8)==2:
            Binary_8='0'+Binary_8
        elif len(Binary_8)==1:
            Binary_8='00'+Binary_8
            
        result=str(int(Binary_8[0])*4+int(Binary_8[1])*2+int(Binary_8[2])*1)+result
        Binary_8=""
        
print(result)
        
    