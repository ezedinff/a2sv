'''
#include <bits/stdc++.h>
#define INF 0x3F3F3F3F
using namespace std;

int main() {
        long long int n,l; cin>>n>>l;
        long long int arr[n+1]; arr[0]=0;
        for(int i =1 ; i<=n;i++) if(i==0) cin>>arr[i]; else {cin>>arr[i]; arr[i]+=arr[i-1];}
        for(int i=0; i<l;i++)
        {
            long long int nu,l=0,h=n; cin>>nu;
            while (l <= h)
               {
                   int m = l + (h-l)/2;
                   if (arr[m-1]<nu&&nu<=arr[m]) {cout<<m<<" "<<nu-arr[m-1]<<endl; break;}
                   if (arr[m] < nu) l = m + 1;
                   else h = m - 1;
               }
        }
    return 0;
}


this code in python

def main():
    n, l = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        a[i] += a[i - 1]

        # print(a)
    
'''

def main():
    n, l = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    for i in range(n):
        x = int(input())
        arr.append(arr[i] + x)

    for i in range(l):
        nu = int(input())
        l, h = 0, n
        while l <= h:
            m = l + (h - l) // 2
            if arr[m - 1] < nu <= arr[m]:
                print(m, nu - arr[m - 1])
                break
            elif arr[m] < nu:
                l = m + 1
            else:
                h = m - 1

main()
