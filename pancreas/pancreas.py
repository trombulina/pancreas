
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def test(a,b):
    return a+b+2
    
def calc_marker_impact(marker_name, data, q = 10):
    data['quantile'] = pd.qcut(data[marker_name],q)
    df2 = data.groupby (['quantile'])['diagnosis'].agg([
        ('all','count'),
        ('control', lambda x: sum([1 if x_i ==1 else 0 for x_i in x])),
        ('benign', lambda x: sum([1 if x_i ==2 else 0 for x_i in x])),
        ('cancer', lambda x: sum([1 if x_i ==3 else 0 for x_i in x])),
    ])
    df2['perc'] = df2['cancer']/df2['all']
    y_1 = df2['perc'].values
    x_1 = df2.index.values
    labels =  [x_i.left for x_i in x_1]
    data.drop(['quantile'], axis='columns', inplace=True)
    return y_1, labels

def draw_lineplot(y,labels,col,fig, title):
    ax = fig.add_subplot(1,1,1)
    x = range(len(y))
    ax.set_xticks( list(x))
    ax.set_xticklabels(labels)
    ax.plot(x, y, marker='o', markerfacecolor=col ,markersize=12, color=col, linewidth=4)
    plt.title(title)
    
colors = cm.rainbow(np.linspace(0, 2, 10))