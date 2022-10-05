'''
Longest Uploaded Prefix

You are given a stream of n videos, each represented by a distinct number from 1 to n that you need to "upload" to a server. You need to implement a data structure that calculates the length of the longest uploaded prefix at various points in the upload process.

We consider i to be an uploaded prefix if all videos in the range 1 to i (inclusive) have been uploaded to the server. The longest uploaded prefix is the maximum value of i that satisfies this definition.You are given a stream of n videos, each represented by a distinct number from 1 to n that you need to "upload" to a server. You need to implement a data structure that calculates the length of the longest uploaded prefix at various points in the upload process.

We consider i to be an uploaded prefix if all videos in the range 1 to i (inclusive) have been uploaded to the server. The longest uploaded prefix is the maximum value of i that satisfies this definition.

Implement the LUPrefix class:

LUPrefix(int n) Initializes the object for a stream of n videos.
void upload(int video) Uploads video to the server.
int longest() Returns the length of the longest uploaded prefix defined above.

Example 1:

Input
["LUPrefix", "upload", "longest", "upload", "longest", "upload", "longest"]
[[4], [3], [], [1], [], [2], []]
Output
[null, null, 0, null, 1, null, 3]
'''

class LUPrefix:
        def __init__(self, n: int):
            self.n = n
            self.uploaded = set()
            self._longest = 0

        def upload(self, video: int) -> None:
            self.uploaded.add(video)
            if video == self._longest + 1:
                self._longest = video
                while self._longest + 1 in self.uploaded:
                    self._longest += 1

        def longest(self) -> int:
            return self._longest

# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
