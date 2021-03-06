import pandas as pd
import os
from library.start import data_path

years = ['yr1112', 'yr1213', 'yr1314', 'yr1415', 'yr1516', 'yr1617', 'yr1718', 'yr1819']

desc_yr1112 = pd.read_csv((os.path.join(data_path, 'tea', 'desc_yr1112.csv')))
desc_yr1213 = pd.read_csv((os.path.join(data_path, 'tea', 'desc_yr1213.csv')))
desc_yr1314 = pd.read_csv((os.path.join(data_path, 'tea', 'desc_yr1314.csv')))
desc_yr1415 = pd.read_csv((os.path.join(data_path, 'tea', 'desc_yr1415.csv')))
desc_yr1516 = pd.read_csv((os.path.join(data_path, 'tea', 'desc_yr1516.csv')))
desc_yr1617 = pd.read_csv((os.path.join(data_path, 'tea', 'desc_yr1617.csv')))
desc_yr1718 = pd.read_csv((os.path.join(data_path, 'tea', 'desc_yr1718.csv')))
desc_yr1819 = pd.read_csv((os.path.join(data_path, 'tea', 'desc_yr1819.csv')))

desc_long = pd.concat([desc_yr1112, desc_yr1213, desc_yr1314, desc_yr1415, desc_yr1516, desc_yr1617, desc_yr1718, desc_yr1819], sort = True)

desc_long.to_csv((os.path.join(data_path, 'tea', 'desc_long.csv')))
