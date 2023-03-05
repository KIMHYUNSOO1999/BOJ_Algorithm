def solution(array):
    
    dict_array={}
    answer=0


    for i in range(len(array)):
        if array[i] not in dict_array:
            dict_array[array[i]]=1
        else:
            dict_array[array[i]]+=1
        
    if len(dict_array) == 1 :                     
        answer = list(dict_array.keys())[0]
    else :                                            
        first_max = sorted(dict_array.values())[-1]
        second_max = sorted(dict_array.values())[-2]  

        if first_max == second_max :                    
            answer = -1
        else:         
            for key, value in dict_array.items() :   
                if value == first_max :
                    answer = key
    return answer