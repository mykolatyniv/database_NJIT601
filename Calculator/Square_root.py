def square_root(a):
    a = int(a)
    c = a**.5
    if c > 10:
        c = round(c, 8)
    else:
        c = round(c, 9)
    return c