# Find Duplicate File in System
# https://leetcode.com/problems/find-duplicate-file-in-system/
# algorithm: hash table
# topics: string

import re
from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_dict = {}
        for path in paths:
            path_split = path.split()
            for file in path_split[1:]:
                file_split = re.split(r'\(|\)', file)
                file_dict.setdefault(file_split[1], []).append(path_split[0] + '/' + file_split[0])
        return [file_dict[key] for key in file_dict if len(file_dict[key]) > 1]