from types import CellType

#%%
# Python code to demonstrate StatisticsError
 
# importing the statistics module
import numpy as np
import matplotlib.pyplot as plt
import statistics
from tracemalloc import Statistic
 
# creating a data-set with one element
x      = np.linspace(1,2000,2000)
sample = np.random.randint(1,3,1000)
data1  = np.random.randint(1,100,200)
data2  = np.random.randint(1,3,800)
data   = np.append(sample,data1)
data   = np.append(data,data2)



# will raise StatisticsError
the_standard_deviation = statistics.stdev(sample)
the_mean = statistics.mean(sample)
print(the_standard_deviation)
print(the_mean)
#plt.scatter(x, data)
plt.plot(x,data)
plt.show()

# %%
