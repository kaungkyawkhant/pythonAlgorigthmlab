# O(n2) | O(1)
# def twoNumSum(array, targetSum):
#     for i in range(len(array)-1):
#         firstNum = array[i]
#         for j in range(i + 1, len(array)):
#             secondNum = array[j]
#             sumResult = firstNum + secondNum
#             if sumResult == targetSum:
#                 return True
#     return False
# O(logn) | O(1)
def twoNumSum(array, targetSum):
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] + array[right] > targetSum:
            right -= 1
        if array[left] + array[right] < targetSum:
            left += 1
        else:
            return True
    return False

print(twoNumSum([1,2,4,4,9,9], 18))
