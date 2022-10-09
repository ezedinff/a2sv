# Time Based Key-value store
# https://leetcode.com/problems/time-based-key-value-store/

# Example 1:
# input: ["TimeMap","set","get","get","set","get","get"]
#        [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
# output: [null,null,"bar","bar",null,"bar2","bar2"]

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}

    # if M is then number of set function call, N is the number of get function calls, and L is
    # the average length of key and value strings
    
    # in set
    # O(L) time to has the string
    # for M calls overall, O(M*L) time
    # time complexity: O(M * L)
    # space complexity: O(M * L)

    # in get
    # O(L) time to has the string
    # we iterate linearly through the timestamp, so O(timestamp) time
    # for N calls overall, O(N * L * timestamp) time
    # time complexity: O(timestamp * N * L)
    # space complexity: O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = {}
        self.data[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        if timestamp in self.data[key]:
            return self.data[key][timestamp]
        for t in range(timestamp, 0, -1):
            if t in self.data[key]:
                return self.data[key][t]
        return ""


# using sorted map and binary search
class TimeMap2:
    
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.data = {}
    
        # in set
        # O(L) time to has the string
        # for M calls overall, O(M*L) time
        # time complexity: O(M * L)
        # space complexity: O(M * L)
    
        # in get
        # O(L) time to has the string
        # we use binary search to find the timestamp, so O(log(timestamp)) time
        # for N calls overall, O(N * L * log(timestamp)) time
        # time complexity: O(log(timestamp) * N * L)
        # space complexity: O(1)
        def set(self, key: str, value: str, timestamp: int) -> None:
            if key not in self.data:
                self.data[key] = SortedDict()
            self.data[key][timestamp] = value
    
        def get(self, key: str, timestamp: int) -> str:
            if key not in self.data:
                return ""
            it = self.data[key].bisect_right(timestamp)
            if it == 0:
                return ""
            return self.data[key].values()[it - 1]
            

if __name__ == "__main__":
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    print(tm.get("foo", 1))
    print(tm.get("foo", 3))
    tm.set("foo", "bar2", 4)
    print(tm.get("foo", 4))
    print(tm.get("foo", 5))