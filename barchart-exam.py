import numpy as np
import matplotlib.pyplot as plt

# data variables
#GDP growth in % of 7 regions of the world, grouped by decades (source https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(real)_per_capita_growth_rate)
gdp_data = [[3.41,	4.95,	3.21,	5.57,	2,	     2.13,  2.80],
            [1.96,	2.92,	2.17,	2.90,	0.67,	 0.94,  3.56],
            [1.34,	2.12,	2.27,	3.63,	3.07,	-1.56,  -0.58],
            [1.32,	1.94,	2.14,	2.49,	3.19,	-0.64,  1.43],
            [1.54,	0.74,	0.73,	3.67,	5.26,	2.86,	1.94],
            [1.63,	1.09,	1.45,	3.70,	5.21,	0.63,	0.23]]

vals = [3.41, 4.95, 3.21, 5.57, 2, 2.13, 2.80]

periods=['1960-1970', '1970-1980', '1980-1990', '1990-2000', '2000-2010', '2010-2018']

zones=['World', 'Eurozone', 'North America', 'E. Asia and Pacific', 'South Asia', 'SS Africa', 'Latin America']

abs_gdp=[[3746, 10733, 17453, 1283, 332, 1115, 3708],
        [10857, 40953, 54261, 10262, 1888, 1659, 9141]]

colors=['m', 'k', 'b', 'g', 'c', 'y']

# x-axis division in 7 zones 
x = np.arange(7)

# defining subplot size
px = 1/plt.rcParams['figure.dpi']  # pixel in inches
fig, ax1 = plt.subplots(figsize = (1024*px, 768*px))

# building a bars group
for idx, val in enumerate(colors):
    ax1.bar(x +(idx/10), gdp_data[idx], color = val, width = 0.1)

# adding y=0 axis
ax1.axhline(linewidth=1, color = 'k', label='_nolegend_')

# building secondary y-axis 
ax2 = ax1.twinx()
ax2.set_ylim(-32400, 100000)
ax2.set_ylabel('Absolute GDP', color = 'r')

# creating a line plot
ax2.plot([x, x + 0.5], [abs_gdp[0], abs_gdp[1]], color = 'r', linewidth = 3)

# adding last decade growth values
for i, v in enumerate(gdp_data[5]):
    ax1.text(i+0.5, v, str(v), color='orange')

# add labels, legend, title
ax1.set_ylabel('GDP growth in %')
ax1.legend(periods)
plt.xticks(x, zones)

# displaying the title
plt.title(label='GDP per capita (constant) annual growth according to the World Bank', fontweight=12, pad='2.0')

# displaying the visualization
plt.show()