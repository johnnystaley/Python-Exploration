# This syntax is used to demonstrate the features of matplotlib pyplot

# Imports matplotlib library
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
#plt.show() # Display the plot.

fig = plt.figure()  # an empty figure with no Axes
fig, ax = plt.subplots()  # a figure with a single Axes
fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
# a figure with one axes on the left, and two on the right:
fig, axs = plt.subplot_mosaic([['left', 'right-top'],
                               ['left', 'right_bottom']])
#plt.show()

#Types of inputs to plotting functions

# Plotting functions expect numpy.array or numpy.ma.masked_array as input, or objects that can be passed 
# to numpy.asarray. Classes that are similar to arrays ('array-like') such as pandas data objects and 
# numpy.matrix may not work as intended. Common convention is to convert these to numpy.array objects 
# prior to plotting. For example, to convert a numpy.matrix

b = np.matrix([[1, 2], [3, 4]])
b_asarray = np.asarray(b)

# Matplotlib allows you to provide the data keyword argument and 
# generate plots passing the strings corresponding to the x and y variables.

np.random.seed(19680801)  # seed the random number generator.
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')
plt.show()

