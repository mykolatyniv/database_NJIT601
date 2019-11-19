def population_standard_deviation(a, b):
    try:
       a = int(a)
       b = int(b)
       c = (a ** 2) / b
       return c
    except ZeroDivisionError:
        print("Error: Wrong number, not valid!!")
    except ValueError:
        print ("Error: Only Numeric Values are valid!!")