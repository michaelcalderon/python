import pandas
import matplotlib.pyplot as plt

pop = pandas.read_csv("gapminder.csv", usecols= [3])
age = pandas.read_csv("gapminder.csv", usecols= [5])
        
plt.scatter(pop, age) # x and y being 2 lists of the coordinates of your values

plt.scatter(pop, age, label='Population vs Life Expectancy')

plt.xlabel('Population')
plt.ylabel('Life Expectancy')
plt.title('Interesting Graph\nBy Michael Calderon')
plt.legend()
plt.show()
