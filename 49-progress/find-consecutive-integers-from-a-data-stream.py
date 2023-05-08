# 2526. Find Consecutive Integers from a Data Stream
# https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/
from collections import deque

class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.currIdx = -1
        self.lastIdx = -1

    def consec(self, num: int) -> bool:
        self.currIdx += 1
        if num != self.value:
            self.lastIdx = self.currIdx
        return self.currIdx - self.lastIdx >= self.k

class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.q = deque()

    def consec(self, num: int) -> bool:
        self.q.append(num)
        if len(self.q) > self.k:
            self.q.popleft()
        return len(self.q) == self.k and all(x == self.value for x in self.q)
    


'''
class Solution {
    public String removeDuplicateLetters(String s) {
        int [] res = new int[26];
        boolean [] vis = new boolean [26];
        char[] chars = s.toCharArray();
        Stack<Character> st = new Stack<>();
        for(char c: chars){
            res[c - 'a']++;
        }
        int index = -1;
        for (char c: chars){
            index = c - 'a';
            res[index] --;
            if (vis[index])
                continue;
            while (!st.isEmpty() && c < st.peek() && res[st.peek() - 'a']!= 0){
                char top = st.pop();
                vis[top - 'a'] = false;
            }
            st.push(c);
            vis[index] = true;

        }

        StringBuilder sb = new StringBuilder();
        while (!st.isEmpty()){
            sb.insert(0, st.pop());
        }
        return sb.toString();
    }
}

to python

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        res = [0] * 26
        vis = [False] * 26
        st = []
        for c in s:
            res[ord(c) - ord('a')] += 1
        index = -1
        for c in s:
            index = ord(c) - ord('a')
            res[index] -= 1
            if vis[index]:
                continue
            while st and c < st[-1] and res[ord(st[-1]) - ord('a')] != 0:
                top = st.pop()
                vis[ord(top) - ord('a')] = False
            st.append(c)
            vis[index] = True
        return ''.join(st)

'''