#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#


'''
Sample Input

5
2 4 6 8 3
Sample Output

2 4 6 8 8 
2 4 6 6 8 
2 4 4 6 8 
2 3 4 6 8 
'''

def insertionSort1(n, arr):
    last = arr[-1]
    for i in range(n-2, -1, -1):
        if arr[i] > last:
            arr[i+1] = arr[i]
            print(*arr)
        else:
            arr[i+1] = last
            print(*arr)
            break
    if arr[0] > last:
        arr[0] = last
        print(*arr)

# explaination:
# we start from the second last element of the array
# if the current element is greater than the last element,
#   we move the current element to the next position
# if the current element is smaller than the last element,
#   we insert the last element to the next position
# Time: O(n)

# what is *arr?
# it is a way to unpack the array and print each element in the array


if __name__ == '__main__':
    n = 2
    arr = [2, 4, 6, 8, 3]

    insertionSort1(n, arr)