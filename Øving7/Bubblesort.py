def bubble_sort( l ):
    done = False
    while done is False:
        done = True
        for i in range( len( l ) - 1 ):
            if l[i] > l[i+1]:
                tmp = l[i+1]
                l[i+1] = l[i]
                l[i] = tmp
                done = False
            else:
                continue
    return l
