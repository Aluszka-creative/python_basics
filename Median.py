# The median is the value separating the higher half from the lower half of a data sample, a population or a probability distribution.

def min(list):
    if len(list) == 0:
        return None
    elif len(list) == 1:
        return list[0]
    else:
        smallest = list[0]
        for i_item in list:
            if i_item < smallest:
                smallest = i_item
    return smallest

def sort_min(list):
    if len(list) == 0:
        return None
    elif len(list) == 1:
        return list[0]
    else:
        copy_list = []
        sorted_list = []
        for i_element in list:
            copy_list.append(i_element)
        for i_index in range(0, len(list)):
            min_element = min(copy_list)
            sorted_list.append(min_element)
            copy_list.remove(min_element)
        return sorted_list

def mean(list):
    if len(list) == 0:
        return None
    elif len(list) == 1:
        return list[0]
    else:
        sum = 0
        quotient = 0
        for i_item in list:
            i_index = list.index(i_item)
            sum += i_item
            quotient += 1
        mean = sum / quotient
        return mean

def count_elements(list):
    number_of = 0
    for i_index in range(len(list)):
        number_of += 1
    return number_of

def number_even(number):
    if  (number % 2) == 0:
        return 1
    else:
        return 0

def median(list):
    if len(list) == 0:
        return None
    elif len(list) == 1:
        return list[0]
    else:
        list_sort = sort_min(list)
        even_list = []
        num_of_elements = int(count_elements(list))
        if number_even(num_of_elements) == 0:
            median_index = int((num_of_elements + 1) / 2)
            median = list_sort[median_index - 1]
        else:
            index_1 = int(num_of_elements / 2)
            median_1 = int(list_sort[index_1 - 1])
            even_list.append(median_1)
            index_2 = int((num_of_elements / 2) + 1)
            median_2 = list_sort[index_2 - 1]
            even_list.append(median_2)
            median = mean(even_list)

        return median





list_ = [1, 3, 2, 5, 4]
print(median(list_))