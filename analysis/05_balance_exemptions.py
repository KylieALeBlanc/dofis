#!/usr/bin/env python
# coding: utf-8

# %%


import os
import sys

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

from dofis.analysis.library import analysis, characteristics, regulations, start, tables


# %%


data_path = start.data_path
table_path = start.table_path
data = pd.read_csv(
    os.path.join(start.data_path, "clean", "master_data_district.csv"), sep=","
)
data = data[data.year == 2016]
data = data[(data.doi == 1)]
data["teachers_turnover_ratio_d"] = data.teachers_turnover_ratio_d / 100

data[data.doi_year < 2020]
# %%

for reg, col in zip(
    [
        "reg25_0811",
        "reg25_081",
        "reg25_0812",
        "reg25_082",
        "reg25_112",
        "reg25_113",
        "reg21_003",
        "reg21_053",
        "reg21_057",
        "reg21_102",
        "reg21_401",
        "reg21_352",
        "reg25_092",
        "reg37_0012",
        "reg25_036",
    ],
    list(range(2, 17)),
):
    teacher = analysis.many_y_one_x(
        data=data,
        y_list=characteristics.teacher,
        y_labels=characteristics.labels,
        x=reg,
    )
    student = analysis.many_y_one_x(
        data=data,
        y_list=characteristics.student,
        y_labels=characteristics.labels,
        x=reg,
    )
    dfs = [teacher, student]
    rows = [7, 16]
    for df, row in zip(dfs, rows):
        tables.just_diff_to_excel(
            file=start.table_path + "balance_exemptions.xlsx",
            df=df,
            diff_col="Difference",
            se_col="Std. Error",
            pvalue_col="P-value",
            start_col=col,
            start_row=row,
        )
    tables.n_to_excel(
        file=start.table_path + "balance_exemptions.xlsx",
        col=col,
        row=5,
        n=data[data[reg] == 1].district.nunique(),
    )
