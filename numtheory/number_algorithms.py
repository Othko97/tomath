"""
A library of useful number theoretical functions
"""

"""
Division function

Returns a | b 
"""
def d(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b % a == 0


"""
Euclidean Algorithm

Takes two nonzero numbers, returns their gcd
"""
def gcd(a, b):
    #Consistently define n, m such that n > m
    n = max((abs(a), abs(b)))
    m = min((abs(a), abs(b)))

    if n == m and n == 0:
        raise ZeroDivisionError
    
    while m != 1:
        t = m #temporary store of m
        m = n - t
        n = m

    return n


"""
Exeuclid(·,·)

The extended Euclidean Algorithm applied to a, b.

Output: gcd(a,b)
        quotlist: list of quotients
"""
def exeuclid(a, b):
    quotlist = []
    n = max((abs(a), abs(b)))
    m = min((abs(a), abs(b)))

    if n == m and n == 0:
        raise ZeroDivisionError

    while m != 1:
        quotlist.append(n // m)
        t = m
        m = n - t
        n = m

    return n, quotlist


"""
Lowest Common Multiple

Returns the lowest common multiple of two nonzero numbers
"""
def lcm(a, b):
    if a == b and a == 0:
        raise ZeroDivisionError
    return int(abs(a) * abs(b) / gcd(a, b))


"""
Bezout(·,·)

Returns a tuple of (s,t) such that as+bt = gcd(a,b)
"""
def Bezout(a, b):
    gcd, quotlist = exeuclid(a, b)
    
