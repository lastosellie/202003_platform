
def quicksort(list):
    length = len(list)
    if length <= 1:
        return list
    pivot = list[len(list) // 2]
    less_list, equal_list, big_list = [], [], []
    for l in list:
        if l < pivot : less_list.append(l)
        elif l > pivot : big_list.append(l)
        else: equal_list.append(l)
    return quicksort(less_list) + equal_list + quicksort(big_list)

list = [6,8,3,9,10,1,2,4,7,5]
print(quicksort(list))
