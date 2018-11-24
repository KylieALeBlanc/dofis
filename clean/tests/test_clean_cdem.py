from unittest import TestCase
from clean.library import clean_tea_schools

class TestClean_cdem(TestCase):
    def test_clean_cdem(self):
        year_list = ['yr1112', 'yr1213', 'yr1314', 'yr1415', 'yr1516', 'yr1617', 'yr1718']
        for year in year_list:
            clean_tea_schools.clean_cdem(year)
        self.assertEqual(1,1)
