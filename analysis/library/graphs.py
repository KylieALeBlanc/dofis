import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf



def create_bar_df(data, group_var, x_var, group_order_dict):
    bar_df = data.groupby([group_var])[x_var].agg({'reg_mean': 'mean', 'reg_std':'std', 'reg_count': 'count'})
    bar_df['order'] = bar_df.index.map(group_order_dict)
    bar_df['sqrtn'] = bar_df['reg_count'].apply(np.sqrt)
    bar_df['se'] = bar_df.reg_std / bar_df.sqrtn
    bar_df = bar_df.reset_index()
    bar_df = bar_df.sort_values('order')
    return bar_df


def create_bar_graph(data, group_col, order_col, y_col, se_col, ylabel, title):
    ci = data[se_col] * 1.98 * 2

    palette = plt.get_cmap('Accent')

    # Create bars
    plt.bar(data[group_col], data[y_col], yerr=ci, color=palette(data[order_col]))

    # Create names on the x-axis
    plt.xticks(data[group_col], fontsize = 16)
    plt.xticks(rotation=90)

    plt.ylabel(ylabel, fontsize = 16)
    plt.title(title, fontsize = 20)

    # Show graphic


#####################################

def barplot_annotate_brackets(num1, num2, data, center, height, yerr=None, dh=.01, barh=.01, fs=None, maxasterix=None):
    """
    Annotate barplot with p-values.

    :param num1: number of left bar to put bracket over
    :param num2: number of right bar to put bracket over
    :param data: string to write or number for generating asterixes
    :param center: centers of all bars (like plt.bar() input)
    :param height: heights of all bars (like plt.bar() input)
    :param yerr: yerrs of all bars (like plt.bar() input)
    :param dh: height offset over bar / bar + yerr in axes coordinates (0 to 1)
    :param barh: bar height in axes coordinates (0 to 1)
    :param fs: font size
    :param maxasterix: maximum number of asterixes to write (for very small p-values)
    """

    if type(data) is str:
        text = data
    else:
        # * is p < 0.05
        # ** is p < 0.005
        # *** is p < 0.0005
        # etc.
        text = ''
        p = .05

        while data < p:
            text += '*'
            p /= 10.

            if maxasterix and len(text) == maxasterix:
                break

        if len(text) == 0:
            text = 'n. s.'

    lx, ly = center[num1], height[num1]
    rx, ry = center[num2], height[num2]

    if yerr:
        ly += yerr[num1]
        ry += yerr[num2]

    ax_y0, ax_y1 = plt.gca().get_ylim()
    dh *= (ax_y1 - ax_y0)
    barh *= (ax_y1 - ax_y0)

    y = max(ly, ry) + dh

    barx = [lx, lx, rx, rx]
    bary = [y, y+barh, y+barh, y]
    mid = ((lx+rx)/2, y+barh)

    plt.plot(barx, bary, c='black')

    kwargs = dict(ha='center', va='bottom')
    if fs is not None:
        kwargs['fontsize'] = fs

    plt.text(*mid, text, **kwargs)