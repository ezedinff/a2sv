'''
#include<bits/stdc++.h>

typedef long long int ll;

#define dbg printf("in\n");
#define nl printf("\n");
#define pp pair<int,int>
#define N 50

using namespace std;

int main()
{
    //freopen("in.txt","r",stdin);

    int i,j,k;
    int n,m,sum;
    string s,t;
    map<char,int> mp;

    cin>>s;

    //if length is less than 26
    if(s.length()<26)
    {
        cout<<"-1";
        return 0;
    }

    i=0,j=25;
    for(k=0;k<26;k++)
        mp[s[k]]++;

    bool f;
    while(j<s.length())
    {
        f=1;
        sum=0;

        //check map
        for(k='A';k<='Z';k++)
        {
            if(mp[k]>1)
            {
                f=0;break;
            }

            else if(mp[k]==0)
                sum++;
        }

        if(!f )
        {
            mp[s[i]]--;
            i++;j++;
            mp[s[j]]++;
            continue;
        }

        //done
        if(sum==mp['?'])
        {
            stack<char> v;
            for(k='A';k<='Z';k++)
            {
                if(!mp[k])
                    v.push(k);
            }

            for(k=i;k<=j;k++)
            {
                if(s[k]=='?')
                    s[k]=v.top(),v.pop();
            }

            //fill the rest of the '?' with 'a'
            for(k=0;k<s.length();k++)
            {
                if(s[k]=='?')
                    s[k]='A';
            }

            cout<<s;
            return 0;
        }
    }

    cout<<"-1";

    return 0;
}

convert this code to python

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()


'''

from collections import defaultdict

n = 50
s = input().strip()

# if length is less than 26
if len(s) < 26:
    print("-1")
    exit()

i, j = 0, 25
mp = defaultdict(int)

for k in range(26):
    mp[s[k]] += 1

while j < len(s):
    f = True
    sum_ = 0

    # check map
    for k in range(ord('A'), ord('Z') + 1):
        if mp[chr(k)] > 1:
            f = False
            break
        elif mp[chr(k)] == 0:
            sum_ += 1

    if not f:
        mp[s[i]] -= 1
        i += 1
        j += 1
        mp[s[j]] += 1
        continue

    # done
    if sum_ == mp['?']:
        v = []
        for k in range(ord('A'), ord('Z') + 1):
            if not mp[chr(k)]:
                v.append(chr(k))

        for k in range(i, j+1):
            if s[k] == '?':
                s = s[:k] + v.pop() + s[k+1:]

        # fill the rest of the '?' with 'a'
        s = s.replace('?', 'A')
        print(s)
        exit()

print("-1")
