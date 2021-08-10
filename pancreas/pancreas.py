
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

    
    
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
    
#Let's create a function to easily draw scatterplots on this data
def plot_scatterplot(var1,var2,data):
    x = data[var1]
    y = data[var2]
    col = [1 if d==3 else 0 for d in data['diagnosis']]
    plt.title('Cancer diagnosis status')
    plt.scatter(x,y, c= col)
    plt.colorbar()
    axes = plt.gca()
    axes.set_ylim([x.quantile(0.05),x.quantile(0.95)])
    axes.set_xlim([y.quantile(0.05),y.quantile(0.95)])
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.show()


colors = cm.rainbow(np.linspace(0, 2, 10))
