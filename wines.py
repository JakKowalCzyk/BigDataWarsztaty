import pandas
import matplotlib.pyplot
import seaborn
import numpy
from os import path

# import pandas_profiling

red_wines = pandas.read_csv(path.realpath('winequality-red.csv'), error_bad_lines=False)
white_wines = pandas.read_csv(path.realpath('winequality-white.csv'), error_bad_lines=False)


print(len(red_wines))
print(len(white_wines))

print(red_wines.shape)
print(white_wines.shape)


print(white_wines.describe())
print(red_wines.describe())