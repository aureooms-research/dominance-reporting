#!/usr/bin/env python3

def pretty ( t ) :
    n = len( t )
    if n == 0 : return
    m = len( t[0] )
    o = [ t[i][j] for i in range( n ) for j in range( m ) ]
    w = max( map( len , map( str , o ) ) )
    d = '{:' + str(w) + 'd}'
    l = ' '.join( [d] * m )
    a = '\n'.join( [l] * n )
    return a.format(*o)

def _P ( m , n ) :
    p = [ [ 1 for j in range( n ) ] for i in range( m ) ]
    for i in range( 1 , m ) :
        for j in range( 1 , n ) :
            p[i][j] = p[i-1][j] + p[i][j-1]
    return p

def P ( m , n = None ) :
    if n is None : n = m
    t = _P(m,n)
    s = pretty(t)
    print(s)

if __name__ == '__main__' :

    import sys

    m , n , *_ = map( int , sys.argv[1:] * 2 + [ 5 , 5 ] )
    P(m, n)
