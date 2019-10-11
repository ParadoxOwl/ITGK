def selection_sort( l ):
    unsorted_l = l.copy()
    sorted_l = []
    while len(sorted_l) != len(l):
        largest_i = 0
        for i in range(len( unsorted_l )):
            if i == 0:
                continue
            elif unsorted_l[i] > unsorted_l[ largest_i ]:
                largest_i = i
            else:
                continue
        sorted_l.insert(0, unsorted_l.pop(largest_i))
    return sorted_l
