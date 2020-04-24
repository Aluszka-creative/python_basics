

def mean(list):
    if list.length == 0:
        return None
    elif list.length == 1:
        return list[0]
    else:
        sum = 0
        quotient = 0

    #foreach (iterowanie po ELEMENTACH)
        for i_item in list:
            i_index = list.index(i_item)
            sum += i_item
            quotient += 1
        mean = sum / quotient
        return mean