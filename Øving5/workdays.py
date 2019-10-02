def is_leap_year ( year ):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False


def weekday_newyear( year ):
    base = 1900
    day = 0
    for y in range( base, year ):
        if is_leap_year( y ):
            day += 2
        else:
            day += 1
        day = day % 7
    return day


def is_workday( day ):
    if day < 5:
        return True
    else:
        return False


def workdays_in_year( year ):
    base = 52*5
    if is_leap_year( year ):
        if weekday_newyear( year ) is 4:
            return base + 1
        elif weekday_newyear( year ) is 5:
            return base
        else:
            return base + 2
    else:
        if is_workday( weekday_newyear( year ) ) is False:
            return base
        else:
            return base + 1


days = [ 'man', 'tir', 'ons', 'tor', 'fre', 'lor', 'son' ]
for y in range(1900, 1920):
    #print( f'{y} {days[weekday_newyear( y )]}' )
    print(f'{y} har {workdays_in_year( y )}arbeidsdager')
