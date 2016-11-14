# max_min_number.py

def find_max_min(num_list):
    """ Function to find the max and min number from
    The given list of numbers and return them as a list

    :param num_list:
    :return [max, min]:
    """
    if len(num_list) > 1:
        try:
            max_num = int(num_list[0])
            min_num = int(num_list[0])
        except ValueError:
            return 'list has items that are not integers'
        for i in range(len(num_list)):
            # if type(num_list[i]) in [str, dict, tuple, set, list]:
            #     continue
            if num_list[i] > max_num:
                max_num = num_list[i]
            else:
                max_num = max_num
            if num_list[i] < min_num:
                min_num = num_list[i]
            else:
                min_num = min_num
        #print(max_num, min_num)
        if max_num == min_num:
            return [len(num_list)]
        return [min_num, max_num]
    return num_list # return num_list if it has only one item
def main():
    num_list = [2, 2,2,2,2,2,2,2,2,2,2,2, 2]
    num_list1 = [2,2,2,2,2,2,2,2,2,2,4,2]
    print(find_max_min(num_list))

if __name__ == '__main__':main()