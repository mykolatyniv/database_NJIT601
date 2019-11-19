
def variance_of_sample_proportion(a,b,c,d,e,f,g,h,j,k):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(e)
        f = int(f)
        g = int(g)
        h = int(h)
        j = int(j)
        k = int(k)
        sample = [a,b,c,d,e,f,g,h,j,k]
        # Count how many people are over the age 80
        i = 0
        occurrence = 0
        while i < len(sample):
            if (sample[i])> 80:
                occurrence = occurrence + 1
            else:
                i = i + 1
            i = i + 1
        # n is population size
        n = len(sample)
        # p is probability
        p = float(occurrence/n)
        var_samp_propor = float((p * (1-p))/n)
        print("variance_of_sample_proportion:",var_samp_propor )
        return var_samp_propor
    except ZeroDivisionError:
        print("Error: Dividing by Zero is not valid!!")
    except ValueError:
        print ("Error: Only Numeric Values are valid!!")