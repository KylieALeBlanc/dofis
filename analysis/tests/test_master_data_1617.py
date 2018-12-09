import unittest
import pandas as pd
import os
from start import data_path


# statistics taken from: https://rptsvr1.tea.texas.gov/perfreport/tapr/2017/state.pdf
class TestCampusDataIntegrity1617(unittest.TestCase):
    def test_number_districts_schools_students(self):
        """
        Statistics taken from # https://tea.texas.gov/WorkArea/DownloadAsset.aspx?id=51539619750
        :return:
        """
        ground_truth_districts = {'yr1617': 1203}
        ground_truth_schools = {'yr1617': 8757}
        ground_truth_students = {'yr1617': 5343834}

        data = pd.read_csv(os.path.join(data_path, 'clean', 'master_data.csv'), sep=",")

        for yr in ['yr1617']:
            data = data[data.year == yr]
            numdistricts = data.district.nunique()
            numschools = data.schools_num.sum()
            numstudents = data.students_num.sum()
            self.assertEqual(numdistricts, ground_truth_districts[yr])
            self.assertEqual(numschools, ground_truth_schools[yr])
            self.assertEqual(numstudents, ground_truth_students[yr])

    def test_scores(self):
        """
        Number of students taken from
        https://tea.texas.gov/Student_Testing_and_Accountability/Testing/State_of_Texas_Assessments_of_Academic_Readiness_(STAAR)/STAAR_Statewide_Summary_Reports_2016-2017/
        Average scores taken from: https://tea.texas.gov/staar/rpt/sum/
        """
        ground_truth_testers_1617 = {'r_3rd_numtakers': 370790,
                                     'r_5th_numtakers': 379532}

        data = pd.read_csv(os.path.join(data_path, 'clean', 'master_data.csv'), sep=",")

        for yr in ['yr1617']:
            data = data[data.year == yr]
            numtakers = data['r_3rd_numtakers'].sum()
            self.assertTrue(numtakers - 50 <= ground_truth_testers_1617['r_3rd_numtakers'] <= numtakers + 50)
            numtakers = data['r_5th_numtakers'].sum()
            self.assertTrue(numtakers - 50 <= ground_truth_testers_1617['r_5th_numtakers'] <= numtakers + 50)


if __name__ == '__main__':
    unittest.main()