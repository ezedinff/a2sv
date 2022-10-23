'''
Given a number find if the product of any contiguous subsequence can be found in another subsequence of the same number.

Example:

54268 -> True since 4 X 2 = 8
5628 -> False since no product of contiguous subsequence can be found in another subsequence.
10220 -> True since 10 X 2 = 20

Note: The input is given as a string

Numbers in the subsequence greater or equal to 10 can be taken into account and we can assume the string is small enough so that recurssion is a possibility.
'''
class Solution:
    def checkSubsequence(self, s: str) -> bool:
        left, right = 0, 1
        # create dictionary to store all numbers and their indices
        d = {}
        for i, num in enumerate(s):
            if num not in d:
                d[num] = [i]
            else:
                d[num].append(i)
    
        while right < len(s):
            m = int(s[left]) * int(s[right])
            if str(m) in d:
                return True
            left += 1
            right += 1
        return False


# if __name__ == '__main__':
#     s = Solution()
#     print(s.checkSubsequence('54268'))
#     print(s.checkSubsequence('5628'))
#     print(s.checkSubsequence('10220'))



def bs(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            return m
        elif arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1

print(bs([1,2,3,4,5,6,7,8,9,10], 1))


def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

    # complexity: O(n^2)
    # space complexity: O(1)


randomOrderList = [2, 5, 1, 3, 4, 7, 6, 8, 9, 0]

print(bubbleSort(randomOrderList))

def insertionSort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

    # complexity: O(n^2)
    # space complexity: O(1)

print(insertionSort(randomOrderList))

def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

    # complexity: O(n^2)
    # space complexity: O(1)

print(selectionSort(randomOrderList))

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res

    # complexity: O(nlogn)
    # space complexity: O(n)
    # approach: divide and conquer
    # steps: 1. divide the array into two halves
    #        2. sort the two halves
    #        3. merge the two halves
    