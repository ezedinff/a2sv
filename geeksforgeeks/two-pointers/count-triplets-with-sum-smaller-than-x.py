# Count triplets with sum smaller than x
# Given an array of distinct integers and a sum value. Find count of triplets with sum smaller than given sum value. Expected Time Complexity is O(n2).
#
# Input: arr[] = {-2, 0, 1, 3}, sum = 2.
# Output: 2

# Time Limit 2.32sec
class Solution:
    def countTriplets(self, arr, n, sum):
        arr.sort()
        ans = 0
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                if arr[i] + arr[l] + arr[r] >= sum:
                    r -= 1
                else:
                    ans += r - l
                    l += 1
        return ans
    '''
    solution in c++
    #include <bits/stdc++.h>
    using namespace std;

    int countTriplets(int arr[], int n, int sum)
{
    sort(arr, arr + n);
    long ans = 0;
    for (int i = 0; i < n - 2; i++) {
        int l = i + 1, r = n - 1;
        while (l < r) {
            if (arr[i] + arr[l] + arr[r] >= sum)
                r--;
            else {
                ans += (r - l);
                l++;
            }
        }
    }
    return ans;
}
    '''
    
    # using binary search
    def countTriplets2(self, arr, n, sum):
        arr.sort()
        count = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                k = self.binarySearch(arr, j + 1, n - 1, sum - arr[i] - arr[j])
                if k != -1:
                    count += k - j
        return count
    
    def binarySearch(self, arr, l, r, x):
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] >= x:
                r = mid - 1
            else:
                l = mid + 1
        return r
    
    # using two pointers with out sorting
    def countTriplets3(self, arr, n, sum):
        ans = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if arr[i] + arr[j] + arr[k] < sum:
                        ans += 1
        return ans

    # using two pointers with hashing
    def countTriplets4(self, arr, n, sum):
        count = 0
        d = {}
        for i in range(n):
            d[arr[i]] = i
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if sum - arr[i] - arr[j] in d:
                    count += 1
        return count