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


def main():
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    print("Average : ",calc_average_temp(num_list))
    print("Min & Max : ",calc_min_max_temp(num_list))
    

if __name__ == "__main__":
    main()