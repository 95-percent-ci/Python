import numpy as np

twoDArray = np.array([[11, 15, 10, 6], 
                      [10, 14, 11, 5],
                      [34, 34, 21, 23],
                      [15, 18, 14, 9]])


def searchTDArray(array: np.array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i, j] == value:
                return f"Value Found at: {i, j}"
            
    return 'The Element Not Found'

print(searchTDArray(twoDArray, 34))
