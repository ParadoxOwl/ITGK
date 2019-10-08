import random


def random_matrise( w, h ):
    matrix= []
    for i in range( h ):
        row = []
        for j in range( w ):
            row.append(random.randint(0,9))
        matrix.append(row)
    return matrix


def print_matrise( matrix, name ):
    print(f'{name}=[')
    ws = ' ' * len( name )
    for r in matrix:
        print( ws + ' ' + str( r ) )
    print( ws + ']' )


def matrise_addisjon( m1, m2 ):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        print("Matrisene er ikke av samme dimensjon")
    else:
        matirx =[]
        for i in range(len(m1)):
            row = []
            for j in range(len(m1[i])):
                row.append( m1[i][j] + m2[i][j] )
            matirx.append(row)
        return matirx
