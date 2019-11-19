def proportion(a,b,c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        ratio = a/b
        propor = c/ratio
        return propor
    except ZeroDivisionError:
        print("Error: Dividing by Zero is not valid!!")
    except ValueError:
        print ("Error: Only Numeric Values are valid!!")