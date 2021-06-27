import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#task1
#Write a Python program to draw a line with suitable label in the x axis, y axis and a title.

data=np.arange(12)
plt.plot(data)
plt.title("X and Y graph")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

#task2
#Write a Python program to draw line charts of the financial data of Alphabet Inc. between October 3, 2016 to October 7, 2016


date=["10-03-16","10-04-16","10-05-16","10-6-16","10-07-16"]
fin_data=[[774.25,776.065002,769.5,772.559998],
          [776.030029,778.710022,772.890015,776.429993],
          [779.309998,782.070007,775.650024,776.469971],
          [779,780.47998,775.539978,776.859985],
          [779.659973,779.659973,770.75,775.080017]
          ]
df=pd.DataFrame(fin_data,index=date)
df.plot.bar()
plt.show()

#task3
#Write a Python program to display the grid and draw line charts of the closing value of Alphabet Inc. between October 3, 2016 to October 7, 2016. Customized the grid lines with linestyle -, width .5. and color blue.
date = ["03-10-16", "04-10-16", "05-10-16", "06-10-16", "07-10-16"]
closing_value = [772.559998, 776.429993, 776.469971, 776.859985, 775.080017]
df = pd.Series(closing_value, index=date)
df.plot.bar(color="yellow", alpha=0.7)
plt.grid(color='blue', linestyle='-', linewidth=.5)
plt.title("Closing value of Alphabet Inc. between October 3, 2016 to October 7, 2016")
plt.xlabel("Date")
plt.ylabel("Closing balance")
plt.show()

#task4
#Write a Python programming to display a bar chart of the popularity of programming Languages
lang = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
pop = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
df = pd.Series(pop, index=lang)
df.plot.bar()
plt.title("The popularity of programming Languages")
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.show()

#Task5
#Write a Python programming to create a pie chart of the popularity of programming Languages.
lang = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
pop = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
df = pd.Series(pop, index=lang)
plt.title("The popularity of programming Languages")
df.plot.pie()
plt.show()

#task6
#Write a Python program to draw a scatter graph taking a random distribution in X and Y and plotted against each other.

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()
