
# Returns the biggest element from a list
def max(list):

    if len(list) == 0:
        return None
    elif len(list) == 1:
        return list[0]
    else:
        biggest = list[0]

        for i_item in list:
            if i_item >= biggest:
                biggest = i_item

        return biggest

# Returns the smallest element from a list
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