def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)
# technique: divide and conquer
# time complexity: O(n log n)
# space complexity: O(log n)
# stable: no
# in-place: yes

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", arr)
    print("Sorted array is", quickSort(arr))