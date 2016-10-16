#!/usr/bin/env python3

import functools

def _P ( m , n ) :
    p = [ [ 1 for j in range( n ) ] for i in range( m ) ]
    for i in range( 1 , m ) :
        for j in range( 1 , n ) :
            p[i][j] = p[i-1][j] + p[i][j-1]
    return p

def _R ( c ) :

    @functools.lru_cache(None)
    def R ( k , u ) :
        if k == 0 :
            return 0
        if u == -1 :
            return 0
        # if u == 0 :
            # return 1
        return R(k-1,u) + 2 * R(k,u-1) + c * 2**u

    return R

def _G ( p, c ) :

    def G ( k , u ) :

        S = 2**u * c

        return S * ( p[k][u+1] - 1 )

    return G

def get_power ( n , b ) :
    if n < 1 :
        raise Exception('{} not a power of {}'.format(n,b) )
    t = n
    p = 0
    while t != 1 :
        x = t // b
        if t != x * b :
            raise Exception('{} not a power of {}'.format(n,b) )
        t = x
        p += 1
    return p

def _T ( c ) :

    R = _R(c)

    def T ( k , N ) :
        u = get_power(N,2)
        r = R(k,u)
        return r

    return T , R

if __name__ == '__main__' :

    import sys

    K , U = map( int, (sys.argv[1:]*2 + [ 5 , 5 ])[:2] )

    RS = '\033[0m'
    KO = '\033[91m'
    OK = '\033[92m'
    WA = '\033[93m'

    c = 1
    p = _P(K+1,U+2)

    T , R = _T( c )
    G = _G(p,c)

    print( 'c = {}'.format(c) )

    for k in range( 1 , K + 1 ) :
        for u in range( 0 , U + 1 ) :
            t = T(k,2**u)
            f = G(k,u)
            s = 'k = {}, u = {}, T(k,2^u) = {}, {}'.format(k,u,t,t/f)
            if t == f :
                co = OK
                print( co + s + RS )
            elif t < f:
                co = WA
                print( co + s + RS )
            else:
                co = KO
                print( co + s + RS )

