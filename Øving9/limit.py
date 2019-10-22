def genereate_list( csv ):
    f = open( csv, 'r' )
    lst = f.read().split( '\n' )
    d = {}
    for i in lst:
        tmp = str(i).split(',')
        if len(tmp) != 2:
            continue
        tmp[0] = tmp[0].strip( '"' )
        tmp[1] = tmp[1].strip( '"' )
        d[tmp[0]] = tmp[1]
    return d


def all_in( d ):
    res = 0
    for k, v in d.items():
        if v == 'Alle':
            res += 1
    return res


def average_ntnu( d ):
    tot = 0
    n = 0
    for k, v in d.items():
        tmp = k.split(' ')
        if tmp[0] == 'NTNU' and v != 'Alle':
            tot += float( v )
            n += 1
    return f'{tot/n:.2f}'


def lowest_stud( d ):
    stud = 0
    pnt = 100
    for k, v in d.items():
        tmp = k.split(' ')
        if v != 'Alle' and float( v ) < pnt:
            stud = k
            pnt = float( v )
    return stud


def uni_dict( d ):
    current_uni, studies, res = '', [], {}
    for k, v in d.items():
        tmp = k.split(' ')
        if current_uni == '':
            current_uni = tmp[0]
        if tmp[0] != current_uni:
            res[current_uni] = studies
            studies.clear()
            current_uni = tmp[0]
        foo = {}
        foo[tmp[2]] = v
        studies.append( foo )
    res[current_uni] = studies
    return res



points = genereate_list( 'poenggrenser_2011.csv' )
print( all_in( points ) )
print( f'Gjennomsnittlig opptaksgrense for NTNU var : {average_ntnu( points )}' )
print( f'Studiet som hadde den laveste opptalsgrensen var: {lowest_stud( points )}')
print( uni_dict( points ) )
