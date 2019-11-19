def variance_of_population_proportion(a, b):
    try:
        a = int(a)
        b = int(b)
        c = (a ** 2) / b
        d = c ** 2
        return d
    except ZeroDivisionError:
        print("Error: Wrong number, not valid!!")
    except ValueError:
        print ("Error: Only Numeric Values are valid!!")