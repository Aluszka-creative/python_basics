# dominanta(pl) - mode(eng)
# The mode of a set of data values is the value that appears most often

# Returns the biggest element from a list
def max_l(list):
    if list.length == 0:
        return None
    elif list.length == 1:
        return list[0]
    else:
        biggest = list[0]

        for i_item in list:
            if i_item > biggest:
                biggest = i_item

        return biggest

# Returns the biggest element from a dictionary
def get_items_with_max_value(dictionary):
    return_list = list()

    list_values = list(dictionary.values())
    if len(list_values) == 0:
        return return_list
    elif len(list_values) == 1:
        return_list.append(dictionary.items()[0])
        return return_list
    else:
        biggest = list_values[0]

        for i_index in range(0, len(list_values)):
            i_value = list_values[i_index]
            i_item = list(dictionary.items())[i_index]

            if i_value == biggest:
                return_list.append(i_item)
            elif i_value > biggest:
                return_list.clear();
                return_list.append(i_item);

        return return_list;

def mode_1(list_1):     # mode only with lists
    list_2 = []
    a = 0
    if len(list_1) == 0:
        return None
    elif len(list_1) == 1:
        return list_1[0]
    else:
        for i_item in list_1:
            for i_check in list_1:
                if i_item == i_check:
                    a += 1
            list_2.append(a)
        b = get_items_with_max_value(list_2)
        c = list_2.index(b)
        d = list[c]
    return d

def mode_2(list):     # mode with lists and dictionaries
    dictionary = {}
    a = 0
    if len(list) == 0:
        return None
    elif len(list) == 1:
        return list[0]
    else:
        for i_item in list:
            for i_check in list:
                if i_item == i_check:
                    a += 1
            dictionary[i_item] = a
            a = 0
        return get_items_with_max_value(dictionary)




list_ = [1, 2, 1, 3, 1, 4, 3, 3, 2, 1, 3]
my_dict = {1: 4, 2: 5, 3: 7}
print('First item shows mode and a second one how many times it occurs: ' + str(mode_2(list_)) + '.')
