def sample_standard_deviation(a, b, c, d, e, f, g, h, j, k):
    try:
        sample = [a, b, c, d, e, f, g, h, j, k]
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
        sample_mean = (a+b+c+d+e+f+g+h+j+k)/(len(sample))
        x_minus_mean_sum = 0
        x_minus_mean_squared = 0
        i = 0
        while i < len(sample):
            x_minus_mean = int(sample[i]) - float(sample_mean)
            x_minus_mean_sum = float(x_minus_mean_sum) + float(x_minus_mean)
            x_minus_mean_squared = x_minus_mean ** 2 + x_minus_mean_squared
            i = i + 1
        sample_variance = x_minus_mean_squared / len(sample)
        stan_dev = round(sample_variance ** 0.5,12)

        # Sample Standard Deviation
        return stan_dev

    except ZeroDivisionError:
        print("Error: Dividing by Zero is not valid!!")
    except ValueError:
        print("Error: Only Numeric Values are valid!!")
