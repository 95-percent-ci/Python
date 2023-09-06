from array import *
from typing import Union

arr1 = array('i', [1,2,3,4,5,6])

arr1.remove(1) ## O(N)
print(arr1)
# arr1.insert(2, 9)

# print(dir(arr1))

def traverseArray(array: array):
    for i in array:  ## O(N)
        print(i) ## O(1)

# traverseArray(arr1)


def accessElement(array: array, index: int):
    if index > len(array):  ## O(1)
        raise ValueError(f"Index Out of Range!") ## O(1)
    else:
        print(array[index]) ## O(1)

# accessElement(arr1, 10)

def LinearSearch(array: array, target:Union[float, int]):
    for i in range(len(array)): ## O(N)
        if array[i] == target: ## O(1)
            return i ## O(1)
    return -1

# print(LinearSearch(arr1, 11))


