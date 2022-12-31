# boyer moore horspool algorithm
def boyerMooreHorspoolSearch(string, pattern) -> bool:
    if not string:
        raise ValueError("string is empty")
    if not pattern:
        raise ValueError("pattern is empty")
    
    n = len(string) # length of the string
    m = len(pattern) # length of the pattern
    skip = {pattern[i]: m - i - 1 for i in range(m - 1)} # skip table or bad character table
    skip["default"] = m
    print(skip)
    i = m - 1
    while i < n:
        print(string[i - m + 1:i + 1], pattern)
        if string[i - m + 1:i + 1] == pattern:
            return True
        i += skip.get(string[i], skip["default"])
    return False

# technique: bad character heuristic
# time complexity: O(nm) worst case and O(n) average case
# space complexity: O(m)
# stable: yes


def findAndReplace(string, pattern, replacement):
    if not string:
        raise ValueError("string is empty")
    if not pattern:
        raise ValueError("pattern is empty")
    
    n = len(string) # length of the string
    m = len(pattern) # length of the pattern
    skip = {pattern[i]: m - i - 1 for i in range(m - 1)} # skip table or bad character table
    skip["default"] = m
    print(skip)
    i = m - 1
    while i < n:
        if string[i - m + 1:i + 1] == pattern:
            string = string[:i - m + 1] + replacement + string[i + 1:]
            i += len(replacement) - m
        i += skip.get(string[i], skip["default"])
    return string


if __name__ == '__main__':
    string = "hello world world"
    pattern = "world"
    print("Given string is", string)
    print("Given pattern is", pattern)
    print("Is pattern in string?", boyerMooreHorspoolSearch(string, pattern))
    print("Given string is", string)
    print("Given pattern is", pattern)
    print("Given replacement is", "universe")
    print("Replaced string is", findAndReplace(string, pattern, "universe"))