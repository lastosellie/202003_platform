
def sort(l_list, r_list):
    list = []
    while len(l_list) > 0 or len(r_list) > 0:
        if len(l_list) > 0 and len(r_list) > 0:
            if l_list[0] > r_list[0]:
                list.append(r_list[0])
                r_list = r_list[1:]
            else:
                list.append(l_list[0])
                l_list = l_list[1:]
        elif len(l_list) > 0:
            list.append(l_list[0])
            l_list = l_list[1:]
        elif len(r_list) > 0:
            list.append(r_list[0])
            r_list = r_list[1:]
    return list

def mergesort(list):
    length = len(list)
    if length <= 1:
        return list
    mid = length // 2
    l_list = mergesort(list[:mid])
    r_list = mergesort(list[mid:])
    return sort(l_list, r_list)

list = [6,8,3,9,10,1,2,4,7,5]
print(mergesort(list))
