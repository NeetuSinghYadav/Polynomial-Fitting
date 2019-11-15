import numpy as np
import sys
import math
from scipy import stats
import matplotlib.pyplot as plt



data = np.loadtxt(sys.argv[1])
xdata=data[:,0]
ydata=data[:,1]


par = np.polyfit(xdata[0:151], ydata[:151], 1, full=True)
slope=par[0][0]
intercept=par[0][1]

print "#",slope, intercept
print "#Wavelength    theta     YFit            "


Yfit =[]
for (i,j) in zip(xdata,ydata):
    Y=slope*i + intercept
    #print i, j, Y
    Yfit.append(Y)


for i, j,k in zip(xdata, ydata, Yfit):
    print i, j, j-k


plt.plot(xdata,ydata, 'k-', label='org')
plt.plot(xdata,Yfit, 'r', label='line_fit')
plt.plot(xdata, ydata-Yfit, label='fitted')
plt.legend()
plt.show()