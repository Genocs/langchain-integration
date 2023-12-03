"""
   This file is used to query the titanic.csv file using pandas. 
"""
import pandas as pd
import matplotlib.pyplot as plt

# Read the csv file into a pandas dataframe
df = pd.read_csv('titanic.csv')

# Print the first 5 rows of the dataframe
df.plot.scatter(x='Fare', y='Survived')

# Show the plot
plt.show()

# print(df.to_string()) 