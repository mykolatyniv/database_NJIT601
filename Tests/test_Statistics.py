import unittest

from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader

from pprint import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_population_mean(self):
        test_data = CsvReader("Tests/Data/mean.csv").data
        pprint(test_data)
        for row in test_data:
           result = int(row['Result'])
           self.assertEqual(self.statistics.mean(row['Value 1'], row['Value 2'], row['Value 3']), result)
           self.assertEqual(self.statistics.result, result)

    def test_median(self):
        test_data = CsvReader("Tests/Data/median.csv").data
        pprint(test_data)
        for row in test_data:
           result = float(row['Result'])
           self.assertEqual(self.statistics.med(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'], row['Value 5'], row['Value 6']), result)
           self.assertEqual(self.statistics.result, result)

    def test_mode(self):
        test_data = CsvReader("Tests/Data/mode.csv").data
        pprint(test_data)
        for row in test_data:
           result = int(row['Result'])
           self.assertEqual(self.statistics.mod(row['Value 1'], row['Value 2']), result)
           self.assertEqual(self.statistics.result, result)

    def test_population_standard_deviation(self):
        test_data = CsvReader("Tests/Data/devi.csv").data
        pprint(test_data)
        for row in test_data:
            result = int(row['Result'])
            self.assertEqual(self.statistics.population(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.statistics.result, result)

    def test_variance_of_population_proportion(self):
        test_data = CsvReader("Tests/Data/variance.csv").data
        pprint(test_data)
        for row in test_data:
           result = int(row['Result'])
           self.assertEqual(self.statistics.variance(row['Value 1'], row['Value 2']), result)
           self.assertEqual(self.statistics.result, result)

    def test_z_score(self):
        test_data = CsvReader("Tests/Data/score.csv").data
        pprint(test_data)
        for row in test_data:
           result = float(row['Result'])
           self.assertEqual(self.statistics.score(row['Value 1'], row['Value 2'], row['Value 3']), result)
           self.assertEqual(self.statistics.result, result)

    def test_standardized_score(self):
        test_data = CsvReader("Tests/Data/score_1.csv").data
        pprint(test_data)
        for row in test_data:
           result = float(row['Result'])
           self.assertEqual(self.statistics.standardized(row['Value 1'], row['Value 2'], row['Value 3']), result)
           self.assertEqual(self.statistics.result, result)

    def test_correlation_coefficient(self):
        test_data = CsvReader("Tests/Data/corr_coef.csv").data
        pprint(test_data)
        for row in test_data:
           result = float(row['Result'])
           self.assertEqual(self.statistics.corr_coef(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'],
                                                 row['Value 5'], row['Value 6'], row['Value 7'], row['Value 8'],
                                                 row['Value 9'], row['Value 10']), float(row['Result']))
           self.assertEqual(self.statistics.result, result)

    def test_confidence_interval(self):
        test_data = CsvReader("Tests/Data/conf_inter.csv").data
        pprint(test_data)
        for row in test_data:
           result = float(row['Result'])
           self.assertEqual(self.statistics.confidence(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'],
                                                 row['Value 5'], row['Value 6'], row['Value 7'], row['Value 8'],
                                                 row['Value 9'], row['Value 10']), float(row['Result']))
           self.assertEqual(self.statistics.result, result)

    def test_population_variance(self):
        test_data = CsvReader("Tests/Data/pop_var.csv").data
        pprint(test_data)
        for row in test_data:
           result = float(row['Result'])
           self.assertEqual(self.statistics.pop_var(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'],
                                                 row['Value 5'], row['Value 6'], row['Value 7'], row['Value 8'],
                                                 row['Value 9'], row['Value 10']), float(row['Result']))
           self.assertEqual(self.statistics.result, result)

    def test_p_value(self):
        test_data = CsvReader("Tests/Data/p_value.csv").data
        pprint(test_data)
        for row in test_data:
           result = int(row['Result'])
           self.assertEqual(self.statistics.value(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4']), result)
           self.assertEqual(self.statistics.result, result)

    def test_proportion(self):
        test_data = CsvReader("Tests/Data/propor.csv").data
        pprint(test_data)
        for row in test_data:
           result = int(row['Result'])
           self.assertEqual(self.statistics.propor(row['Value 1'], row['Value 2'], row['Value 3']), result)
           self.assertEqual(self.statistics.result, result)

    def test_sample_mean(self):
        test_data = CsvReader("Tests/Data/samp_mean.csv").data
        pprint(test_data)
        for row in test_data:
           result = int(row['Result'])
           self.assertEqual(self.statistics.samp_mean(row['Value 1'], row['Value 2'], row['Value 3']), result)
           self.assertEqual(self.statistics.result, result)

    def test_sample_standard_deviation(self):
        test_data = CsvReader("Tests/Data/samp_stan_dev.csv").data
        pprint(test_data)
        for row in test_data:
           result = float(row['Result'])
           self.assertEqual(self.statistics.stan_dev(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'],
                                                 row['Value 5'], row['Value 6'], row['Value 7'], row['Value 8'],
                                                 row['Value 9'], row['Value 10']), float(row['Result']))
           self.assertEqual(float(self.statistics.result), result)



    def test_variance_of_sample_proportion(self):
        test_data = CsvReader("Tests/Data/var_samp_propor.csv").data
        pprint(test_data)
        for row in test_data:
           result = float(row['Result'])
           self.assertEqual(self.statistics.var_samp_propor(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'],
                                                 row['Value 5'], row['Value 6'], row['Value 7'], row['Value 8'],
                                                 row['Value 9'], row['Value 10']), float(row['Result']))
           self.assertEqual(self.statistics.result, result)


    def test_results_property(self):
        self.assertEqual(self.statistics.result, 0)

if __name__ == '__main__':
        unittest.main()
