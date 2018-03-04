'''Open CSV File Directly and Print Results into Terminal'''
with open('titanic_sub.csv', 'r') as csv_file:
    print(csv_file.read())


'''Load data into numpy array - good for machine learning models bad for multiple data types'''
import numpy as np

filename = 'mnist.csv'
data = np.loadtxt(filename, delimiter=',')
print(data)


'''Gen From Text is Good for Mixed Data Types'''
titanic = 'titanic_sub.csv'
data = np.genfromtxt(titanic, delimiter=',', names=True, dtype=None)
print(data['Survived'])


'''Similar to gen from text but dtype is set to None'''
data = np.recfromcsv(titanic)
# Print out first three entries of d
print(data[:3])

'''Pandas dataframe is the superior way to analyze data and closes the gap between Python & R'''
import pandas as pd

data = pd.read_csv('titanic_sub.csv')
print(data.head())
