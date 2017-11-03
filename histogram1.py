import pandas
import matplotlib.pyplot as plt


x = pandas.read_csv("gapminder.csv", usecols= [5])
        
plt.hist(x)
plt.show()
