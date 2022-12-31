# naive string search algorithm
def naiveSearch(string, pattern) -> bool:
    if not string:
        raise ValueError("string is empty")
    if not pattern:
        raise ValueError("pattern is empty")
    
    n = len(string) # length of the string
    m = len(pattern) # length of the pattern
    for i in range(n - m + 1):
        print(string[i:i + m], pattern)
        if string[i:i + m] == pattern:
            return True
    return False

# technique: brute force
# time complexity: O(n * m) worst case and O(n + m) average case
# space complexity: O(1)
# stable: yes


if __name__ == '__main__':
    string = "hello world"
    pattern = "world"
    print("Given string is", string)
    print("Given pattern is", pattern)
    print("Is pattern in string?", naiveSearch(string, pattern))