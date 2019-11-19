def p_value(a,b,c,d,):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        #Significance level = 0.05
        # Degrees of Freedom
        obs_exp = [a, b, c, d]
        n = len(obs_exp)
        # Degrees of Freedom
        dof = n - 1
        chi_square = float(((a - c) ** 2) / c) + (((b- d) ** 2) / d)
        # chi square distribution table look up value for 0.05 and chi
        return chi_square
    except ZeroDivisionError:
        print("Error: Dividing by Zero is not valid!!")
    except ValueError:
        print ("Error: Only Numeric Values are valid!!")
