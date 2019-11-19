from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.median import median
from Statistics.mode import mode
from Statistics.population_standard_deviation import population_standard_deviation
from Statistics.variance_of_population_proportion import variance_of_population_proportion
from Statistics.z_score import z_score
from Statistics.standardized_score import score
from Statistics.correlation_coefficient import correlation_coefficient
from Statistics.confidence_interval import confidence_interval
from Statistics.population_variance import population_variance
from Statistics.p_value import p_value
from Statistics.proportion import proportion
from Statistics.sample_mean import sample_mean
from Statistics.sample_standard_deviation import sample_standard_deviation
from Statistics.variance_of_sample_proportion import variance_of_sample_proportion


class Statistics(Calculator):
    result = 0

    def __init__(self):
        super().__init__()

    def mean(self, a, b, c):
        self.result = mean(a, b, c)
        return self.result

    def med(self, a, b, c, d, e, f):
        self.result = median(a, b, c, d, e, f)
        return self.result

    def mod(self, a, b):
        self.result = mode(a, b)
        return self.result

    def population(self, a, b):
        self.result = population_standard_deviation(a, b)
        return self.result

    def variance(self, a, b):
        self.result = variance_of_population_proportion(a, b)
        return self.result

    def score(self, a, b, c):
        self.result = z_score(a, b, c)
        return self.result

    def standardized(self, a, b, c):
        self.result = score(a, b, c)
        return self.result

    def corr_coef(self, a, b, c, d, e, f, g, h, j, k):
        self.result = correlation_coefficient(a, b, c, d, e, f, g, h, j, k)
        return self.result

    def confidence(self, a, b, c, d, e, f, g, h, j, k):
        self.result = confidence_interval(a, b, c, d, e, f, g, h, j, k)
        return self.result

    def pop_var(self, a, b, c, d, e, f, g, h, j, k):
        self.result = population_variance(a, b, c, d, e, f, g, h, j, k)
        return self.result

    def value(self, a, b, c, d):
        self.result = p_value(a, b, c, d)
        return self.result

    def propor(self, a, b, c):
        self.result = proportion(a, b, c)
        return self.result

    def samp_mean(self, a, b, c ):
        self.result = sample_mean(a, b, c)
        return self.result

    def stan_dev(self, a, b, c, d, e, f, g, h, j, k):
         self.result = sample_standard_deviation(a, b, c, d, e, f, g, h, j, k)
         return self.result

    def var_samp_propor(self, a, b, c, d, e, f, g, h, j, k):
        self.result = variance_of_sample_proportion(a, b, c, d, e, f, g, h, j, k)
        return self.result


