class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        length = len(arr)
        answer = []
        i = length
        while i > 0:
            max_local = max(arr[:i])
            if arr[i - 1] != max_local:
                k = arr.index(max_local)
                arr_left = arr[:k + 1]
                arr_right = arr[k + 1:]
                arr_left.reverse()
                arr = arr_left + arr_right
                answer.append(k + 1)

                arr_left = arr[:i]
                arr_right = arr[i:]
                arr_left.reverse()
                arr = arr_left + arr_right
                answer.append(i)
            i -= 1
        return answer