def sample_mean(a,b,c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        list_count = [a, b, c]
        n = len(list_count)
        samp_mean = (a + b + c )/n
        return samp_mean
    except ZeroDivisionError:
        print("Error: Dividing by Zero is not valid!!")
    except ValueError:
        print ("Error: Only Numeric Values are valid!!")