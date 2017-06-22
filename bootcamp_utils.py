"""all useful function in bootcamp"""
import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns
sns.set()

#set up personal prefer
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 20})


def ecdf(data):
    x= np.sort(data)
    y= np.arange(1,len(data)+1)/len(data)

    return (x,y)
xa_high = np.loadtxt('data/xa_high_food.csv',comments= '#')

(x,y) = ecdf(xa_high)

#build figure
fig, ax =plt.subplots(1,1)
ax.set_xlabel('number')
ax.set_ylabel('ECDF')

#plot figure
_ = ax.plot(x,y, marker='.', linestyle='none')
