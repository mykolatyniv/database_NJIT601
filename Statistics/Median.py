def median(a, b, c, d, e, f):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(e)
        f = int(f)
        med = [a, b, c, d, e, f]
        n = len(med)
        s = sorted(med)
        f = (sum(s[n // 2 - 1:n // 2 + 1]) / 2.0, s[n // 2])[n % 2] if n else None
        return f
    except ZeroDivisionError:
        print("Error: Wrong number, not valid!!")
    except ValueError:
        print ("Error: Only Numeric Values are valid!!")
