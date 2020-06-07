"""
Four Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
The function should find all quadruplets in the array that sum up to the target sum
and return a two-dimensional array of all these quadruplets in no particular order.

If no four numbers sum up to the target sum, the function should return an empty array.

Sample input: [7, 6, 4, -1, 1, 2], 16
Sample output: [[7, 6, 4, -1], [7, 6, 1, 2]]
"""
def FourNumSum(array, targetSum):
    dict1 = {}
    list1 = []
    for i in range(len(array)-1):
        for j in range(0, len(array)):
            currentSum = array[i] + array[j]
            diffSum = targetSum - currentSum
            if diffSum in dict1:
                list1.append()