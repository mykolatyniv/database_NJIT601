def mode(a, b):
    try:
        a = int(a)
        b = int(b)
        c = a + b
        return c
    except ZeroDivisionError:
        print("Error: Wrong number, not valid!!")
    except ValueError:
        print ("Error: Only Numeric Values are valid!!")
