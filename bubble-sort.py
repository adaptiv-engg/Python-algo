
def bubble_sort(input_list): 
    for x in range(0,len(input_list) - 1):  
        for y in range(len(input_list) - 1):  
            if(input_list[y] > input_list[y+1]):  
                temp = input_list[y]  
                input_list[y] = input_list[y+1]  
                input_list[y+1] = temp  
    return input_list
    
input_list = [5, 3, 8, 6, 7, 2]  
print("Input list: ", input_list)  
# Calling the bubble sort function  
print("Sorted list: ", bubble_sort(input_list))  
