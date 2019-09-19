def alt_sum(n):
    ans = 0
    for i in range( n + 1 ):
        if i%2 is 0:
            ans -= i**2
        else:
            ans += i**2
    return ans


def alt_sum_k(k):
    i = 0
    prev_sum = 0
    ans = 0
    while ans <= k:
        prev_sum = ans
        if i%2 is 0:
            ans -= i**2
        else:
            ans += i**2
        i += 1
    i -= 2
    return prev_sum, i


lim = int( input( 'k = ' ) )
foo = alt_sum_k(lim)
print( f'Summen av tallene før summen blir større en k er {foo[0]}. Antall iterasjoner: {foo[1]}' )
