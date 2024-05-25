# Save and Writing Files using numpy

print('Example.1: Saving a Numpy Array to a Text File (.txt)')

import numpy as np

# Create a sample NumPy array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Save the array to a text file
np.savetxt('array.txt', array, delimiter=',')

# To read the array back from the text file
loaded_array = np.loadtxt('array.txt', delimiter=',')
print(loaded_array)

print('Example.2: Saving a Numpy Array to a Binary File (.npy)')

import numpy as np

# Create a sample NumPy array
array = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# Save the array to a binary file
np.save('array.npy', array)

# To read the array back from the binary file
loaded_array = np.load('array.npy')
print(loaded_array)

print('Example.3: Saving a Multiple Arrays to a Compressed File (.npz)')

import numpy as np

# Create sample NumPy arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.array([7, 8, 9])

# Save the arrays to a compressed file
np.savez('arrays.npz', array1=array1, array2=array2, array3=array3)

# To read the arrays back from the compressed file
loaded = np.load('arrays.npz')
print(loaded['array1'])
print(loaded['array2'])
print(loaded['array3'])


#Load data from files using numpy

print('Example.1: Loading Data from a Text File (.txt)')

import numpy as np

# Assume the file 'data.txt' contains:
# 1.0, 2.0, 3.0
# 4.0, 5.0, 6.0
# 7.0, 8.0, 9.0

# Load the array from the text file
data = np.loadtxt('data.txt', delimiter=',')
print(data)

print('Example.2: Loading Data from a Binary File (.npy)')

import numpy as np

# Assume the file 'data.npy' contains a saved array

# Load the array from the binary file
data = np.load('data.npy')
print(data)

print('Example.3: Loading Multiple Arrays from a Compressed File (.npz)')

import numpy as np

# Assume the file 'data.npz' contains multiple saved arrays

# Load the arrays from the compressed file
loaded_data = np.load('data.npz')

# Accessing each array by its name
array1 = loaded_data['array1']
array2 = loaded_data['array2']
array3 = loaded_data['array3']

print(array1)
print(array2)
print(array3)
