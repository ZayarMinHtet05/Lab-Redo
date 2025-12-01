def display_main_menu():
    print("Enter some numbers separated by commas (eg. 5, 67, 32)")

def get_user_input():
    user_input = input ()
    
    string_list = user_input.split(",")

    float_list = []
    for num_str in string_list:
        float_list.append(float(num_str))

    return float_list

def calc_average_temp(num_list):
    total = sum(num_list)
    average = total/len(num_list)
    return average

def calc_min_max_temp(num_list):
    Minimum = min(num_list)
    Maximum = max(num_list)
    return Minimum,Maximum

def calc_median_temp(num_list):
    sorted_list = sorted(num_list)
    length = len(sorted_list)
    if length %2 == 0:
        mid1 = length//2-1
        mid2 = length//2
        median = (sorted_list[mid1]+sorted_list[mid2])/2
        return median
    else: 
        mid = length//2
        median = sorted_list[mid] 
        return median

def main():
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    print("Average : ",calc_average_temp(num_list))
    print("Min & Max : ",calc_min_max_temp(num_list))
    print("Median : ",calc_median_temp(num_list) )
    

if __name__ == "__main__":
    main()