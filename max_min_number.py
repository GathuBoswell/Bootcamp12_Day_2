# max_min_number.py

def find_max_min(num_list):
    """ Function to find the max and min number from
    The given list of numbers and return them as a list

    :param num_list:
    :return [max, min]:
    """
    max_num = num_list[0]
    min_num = num_list[0]
    for i in range(len(num_list)):
        if num_list[i] > max_num:
            max_num = num_list[i]
            if num_list[i] < min_num:
                min_num = num_list[i]
            min_num = min_num
        max_num = max_num
    return max_num, min_num

def main():
    num_list = [1,2,3,4,5,6]
    print(find_max_min(num_list))

if __name__ == '__main__':main()