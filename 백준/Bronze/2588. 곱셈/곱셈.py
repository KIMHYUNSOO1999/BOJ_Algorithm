number = int(input())  
number2 = input()       

multiply=[]

multiply.append(number * int(number2[2]))
multiply.append(number * int(number2[1]))
multiply.append(number * int(number2[0]))
multiply.append(number * int(number2))

for row in multiply:
    print(row)