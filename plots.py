import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from numpy import genfromtxt

df=pd.read_csv('Book2.csv', sep=',')
print(df['No of messages'].values)
plt.plot(df['No of Nodes'],df['No of messages'], marker='o')

#plt.title('Data from the CSV File: People and Expenses')

#plt.xlabel('No of edges')
#plt.ylabel('No of messages')
#
#plt.show()
lines=df.plot.line(x='No of Nodes', y='No of messages')

plt.show()
