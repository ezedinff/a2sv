class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10**9 + 7
        counter = Counter(deliciousness)
        max_v = max(list(counter.keys()))
        max_pow = 0
        while max_v:
            max_pow += 1
            max_v >>= 1
        pd = [2**i for i in range(max_pow+1)]
        m = collections.defaultdict(int)
        res = 0
        for k, v in sorted(list(counter.items())):
           
            if k > pd[0]:
                del(pd[0])
            
            if k*2 in pd:
                res += v*(v-1)//2
                
            res += m[k]*v
            for p in pd:
                m[p-k] += v
            res %= 10**9+7
            
        return res

