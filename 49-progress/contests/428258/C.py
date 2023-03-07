'''
#include <bits/stdc++.h>
using namespace std;

#define ebar_khela_jombe_besh   int main (void)
#define jitsen_bhai		return 0
#define sf                  	scanf
#define pf                  	printf
#define ssf                 	sscanf
#define spf                 	sprintf
#define fsf                 	fscanf
#define fpf                 	fprintf
#define fast                	ios_base::sync_with_stdio(0),cin.tie(0),cout.tie(0)
#define scase               	sf ("%d",&tc)
#define sn                  	sf ("%d",&n)
#define whilecase           	while (tc--)
#define eof                 	while (cin >> n)
#define forloop             	for (pos=1; pos<=tc; pos++)
#define arrayloop           	for (i=0; i<n; i++)
#define cinstr              	cin >> str
#define getstr              	getline (cin,str)
#define pcase               	pf ("Case %d: ",pos)
#define vi                  	vector <int>
#define si                  	set <int>
#define vs                  	vector <string>
#define pii                 	pair <int,int>
#define mii                 	map <int,int>
#define msi			            map <string,int>
#define pb                  	push_back
#define in                  	insert
#define llu                 	unsigned long long
#define lld                 	long long
#define U                   	unsigned int
#define endl                	"\n"

const int MOD = 1000000007;
const int MAX = 1000005;

int SetBit (int n, int x) { return n | (1 << x); }
int ClearBit (int n, int x) { return n & ~(1 << x); }
int ToggleBit (int n, int x) { return n ^ (1 << x); }
bool CheckBit (int n, int x) { return (bool)(n & (1 << x)); }

int arr[105];
char str[35];

ebar_khela_jombe_besh
{
    /*
    	freopen ("input.txt","r",stdin);
    	freopen ("output.txt","w",stdout);
    */

    int n,m,i,a,b,l,p;

    while (sf ("%d %d",&n,&m) != EOF)
    {
        for (i=0; i<n; i++)
            sf ("%d",&arr[i]);

        msi mp;
        msi :: iterator it;

        for (i=0; i<m; i++)
        {
            sf ("%s",str);
            ++mp[str];
        }

        vi v;

        for (it=mp.begin(); it!=mp.end(); it++)
            v.pb(it->second);

        p = l = v.size();
        a = b = 0;

        sort (arr,arr+n);
        sort (v.begin(),v.end());

        for (i=0; i<l; i++)
            a += arr[i]*v[l-1-i];

        for (i=n-1; i>=n-l; i--)
            b += arr[i]*v[--p];

        pf ("%d %d\n",a,b);

        v.clear();
        mp.clear();
    }

    jitsen_bhai;
}

in python looks like this

    
        
'''

'''
input:
6 5
3 5 1 6 8 1
peach
grapefruit
banana
orange
orange

output:
30 25

'''
from collections import defaultdict

def main():
    while True:
        try:
            n, m = map(int, input().split())
        except EOFError:
            break

        arr = list(map(int, input().split()))

        mp = defaultdict(int)

        for i in range(m):
            word = input().strip()
            mp[word] += 1

        v = list(mp.values())
        l = len(v)
        p = l
        a = b = 0

        arr.sort()
        v.sort()

        for i in range(l):
            a += arr[i] * v[l-1-i]

        for i in range(n-1, n-1-l, -1):
            b += arr[i] * v[p-1]
            p -= 1

        print(a, b)

if __name__ == '__main__':
    main()

