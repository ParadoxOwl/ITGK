import math


def f( x ):
    return ( x - 12 ) * math.exp( x / 2 ) - 8 * ( x + 2 ) ** 2


def g( x ):
    return -x -2*x**2 - 5 * x**3 + 6 * x**4


def differentiate( x_k, x_k1, func ):
    return ( func( x_k ) - func( x_k1 ) ) / ( x_k - x_k1 )


def secant_method( x_k, x_k1, func, tol ):
    while abs( func( x_k ) ) > tol:
        temp = x_k
        x_k -= func( x_k ) / differentiate( x_k, x_k1, func )
    return x_k


def print_secant( x_k, x_k1, func, tol ):
    x = secant_method( x_k, x_k1, func, tol )
    print( f'Funksjonen nærmer seg et nullpunkt når x = {x:.2f} da er f(x) = {func( x ):.2e}' )


print( f( 0 ) )
print( g( 1 ) )
print( differentiate( 10, 9, f ) )
print_secant( 11, 13, f, 0.00001 )
print_secant( 1, 2, g, 0.00001 )
print_secant( 0, 1, g, 0.00001 )
