def geo_n( r, n ):
    result = 0
    for i in range( n + 1 ):
        result += r**i
    return result


def geo_t( r, t ):
    result = 0
    itr = 0
    limit = 1/(1-r)
    while abs( limit - result ) > t:
        result += r**itr
        itr += 1
    return result


def geo_t_itr_dif( r, t ):
    result = 0
    itr = 0
    limit = 1/(1-r)
    while abs( limit - result ) > t:
        result += r**itr
        itr += 1
    return itr - 1, abs( limit - result )


foo = geo_t_itr_dif(0.5, 0.001)
print(f'Påkrevde iterasjoner: {foo[0]}\nDifferanse: {foo[1]}')
