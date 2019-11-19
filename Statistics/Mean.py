def mean(a, b, c):
    try:
       a = int(a)
       b = int(b)
       c = int(c)
       d = (a + b) / c
       return d
    except ZeroDivisionError:
        print("Error: Wrong number, not valid!!")
    except ValueError:
        print ("Error: Only Numeric Values are valid!!")