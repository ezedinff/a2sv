'''
911. Online Election
'''
from typing import List

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.persons = persons
        self.leads = {}
        max_lead = 0
        for i in range(len(persons)):
            if persons[i] not in self.leads:
                self.leads[persons[i]] = 0
            self.leads[persons[i]] += 1
            if self.leads[persons[i]] >= max_lead:
                max_lead = self.leads[persons[i]]
                self.leads[persons[i]] = i

    def q(self, t: int) -> int:
        for i in range(len(self.times)):
            if self.times[i] > t:
                return self.persons[i-1]
        return self.persons[-1]
        
                
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)