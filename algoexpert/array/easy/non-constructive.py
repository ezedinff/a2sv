def nonConstructiveChange(arr):
    arr = sorted(arr)
    prev = 0
    curr = 0
    while prev + 1 >= arr[curr]:
        prev += arr[curr]
        curr += 1
    return prev + 1


if __name__ == '__main__':
    arr = [5, 7, 1, 1, 2, 3, 22]
    print(nonConstructiveChange(arr))
