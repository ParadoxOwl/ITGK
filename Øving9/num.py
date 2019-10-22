def number_of_lines( file ):
    f = open( file, 'r' )
    lines = f.read().split( '\n' ).copy()
    f.close()
    return len( lines )


def number_frequency( file ):
    f = open( file, 'r' )
    nums = f.read().split( '\n' ).copy()
    f.close()
    res = {}
    for n in nums:
        n = int( n )
        try:
            res[n] += 1
        except KeyError:
            res[n] = 1
    print_dict( res )


def print_dict( d ):
    for k, v in d.items():
        print( f'{k}: {v}' )


number_frequency( 'numbers.txt' )
