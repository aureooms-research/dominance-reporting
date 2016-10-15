#!/usr/bin/env python3

import functools

def _P ( m , n ) :
    p = [ [ 1 for j in range( n ) ] for i in range( m ) ]
    for i in range( 1 , m ) :
        for j in range( 1 , n ) :
            p[i][j] = p[i-1][j] + p[i][j-1]
    return p

def _R ( a , b , g ) :

    @functools.lru_cache(None)
    def R ( k , u ) :
        if k == 0 :
            return 0
        if u == -1 :
            return 0
        return a * R(k-1,u) + a * R(k,u-1) + g * b**u

    return R

def _F ( a , b , g ) :

    def F ( k , u ) :

        return ( ((a//b)**(u+1)-1) // (a//b-1) ) * ( (a**k-1) // (a-1) ) * b**u * g

    return F

def _G ( a , b , g ) :

    def G ( k , u ) :

        S = b**u * g

        # ! coeff is wrong in T2 T3
        # T1 = sum( (a//b+a)**i for i in range( 0 , u+k ) )
        # T2 = sum( (a//b+a)**i for i in range( 0 , u ) ) * a**(k)
        # T3 = sum( (a//b+a)**i for i in range( 0 , k-1 ) ) * (a//b)**(u+1)
        # return ( T1 - T2 - T3 ) * S

        p = _P(u+1,k)

        return S * sum( sum( ( a**(i+j) // b**i * p[i][j] ) for j in range(k) ) for i in range( u + 1 ) )

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

def _T ( c , r , d ) :

    logr2 = get_power(r,2)

    a = c * r**(2*d)
    b = r**(d+1)
    g = c * r**(d-1) * d * logr2

    R = _R(a,b,g)

    def T ( k , N ) :
        u = get_power(N,b)
        r = R(k,u)
        return r

    return T , R , a , b , g

if __name__ == '__main__' :

    RS = '\033[0m'
    KO = '\033[91m'
    OK = '\033[92m'
    WA = '\033[93m'

    c = 10
    r = 2**8
    d = 2

    T , R , a , b , g = _T( c , r , d )
    F = _F(a,b,g)
    G = _G(a,b,g)

    print( 'c = {}'.format(c) )
    print( 'r = {}'.format(r) )
    print( 'd = {}'.format(d) )
    print( 'a = {}'.format(a) )
    print( 'b = {}'.format(b) )
    print( 'g = {}'.format(g) )

    for k in range( 1 , 10 ) :
        for u in range( 0 , 10 ) :
            t = T(k,b**u)
            f = G(k,u)
            r = f/t
            s = 'k = {}, u = {}, T(k,b^u) = {}, F(k,u) = {}, {}'.format(k,u,t,f,r)
            co = OK if t == f else ( WA if t < f else KO )
            print( co + s + RS )

