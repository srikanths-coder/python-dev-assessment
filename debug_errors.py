def calculate_average(numbers):
    try: 
         total = 0
         for i in range(len(numbers)):
                total += numbers[i]
                 
                return total / len(numbers)
    except ZeroDivisionError:
          return 0   
    
data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = []
print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}")

def get_list_element(my_list, index):
    try:
       
        return my_list[index]
    
    except IndexError:
        
        print(f"Error: Index {index} is out of bounds.")
        return None


if __name__ == "__main__":
   
    print(get_list_element([10, 20, 30], 1)) 

    
    print(get_list_element([10, 20, 30], 5)) 

    
    print(get_list_element([10, 20, 30], -1)) 
