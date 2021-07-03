import pandas as pd
import numpy as np
#from googletrans import Translator
import matplotlib.pyplot as plt
import csv

df = pd.read_csv("Other/Data_Project_2.csv")
df["number"] = df["number"].replace('.', '')
df['number'] = df['number'].replace(0, np.nan)
df = df.dropna()
a = pd.Series(df["number"], index=df["year"])
# Graph by years
# a.plot.bar()
# plt.title("Amazon Fires by Years")
# plt.show()

b = pd.Series(df["number"], index=df["month"])
# Graph by months
# b.plot.bar()
# plt.title("Amazon Fires by Months")
# plt.show()

c = df.groupby(['month'])['number'].agg('sum')
c.reindex(["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Janeiro", "Agosto", "Setembro", "Outubro",
          "Novembro", "Dezembro"])
print(c)
