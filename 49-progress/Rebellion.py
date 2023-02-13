# https://codeforces.com/problemset/problem/1746/B

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        array_size = int(input())
        array = list(map(int, input().split()))
        print(minimum_flip_operations(array_size, array))

def minimum_flip_operations(array_size, array) -> int:
    contains_one = False
    for i in range(array_size):
        if array[i] == 1:
            contains_one = True
    if not contains_one:
        return 0
    zeros_indices = []
    ones_indices = []
    for i in range(array_size-1, -1, -1):
        if array[i] == 0:
            zeros_indices.append(i)
    for i in range(array_size):
        if array[i] == 1:
            ones_indices.append(i)
    operations = 0
    while True:
        if not zeros_indices or not ones_indices:
            break
        zero_index = zeros_indices[0]
        one_index = ones_indices[0]
        if one_index > zero_index:
            break
        zeros_indices.pop(0)
        ones_indices.pop(0)
        operations += 1
    return operations
