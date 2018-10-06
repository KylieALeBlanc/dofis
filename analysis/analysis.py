import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

def create_count_proportion_df(data, list_of_regs, dict_of_reg_labels):
    n_col = []
    p_urban = []
    p_suburb = []
    p_town = []
    p_rural = []
    reg_labels = []
    f_p = []

    for reg in list_of_regs:
        n_col.append((len(data[data[reg] == 1])))
        p_urban.append(data[data.type_urban == 1][reg].mean().round(2))
        p_suburb.append(data[data.type_suburban == 1][reg].mean().round(2))
        p_town.append(data[data.type_town == 1][reg].mean().round(2))
        p_rural.append(data[data.type_rural == 1][reg].mean().round(2))
        reg_labels.append(dict_of_reg_labels[reg])
        formula = reg + '~ type_urban + type_suburban + type_town + type_rural - 1'
        df = data.dropna(subset=['type_urban', 'type_suburban', 'type_town', 'type_rural', reg])
        results = smf.ols(formula, data=df).fit()
        f_p.append(results.f_pvalue.round(2))

    df = pd.DataFrame(
            {'Regulation': reg_labels,
             'Count': n_col,
             'Percent Urban': p_urban,
             'Percent Suburban': p_suburb,
             'Percent Town': p_town,
             'Percent Rural': p_rural,
             'F-test p-value': f_p
             })

    return df