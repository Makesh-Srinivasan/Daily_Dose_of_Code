class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()  #count[num] = number of occurances/count

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)


        freq = [[] for i in range(len(nums)+1)]
        for n,c in count.items():
            freq[c].append(n)


        res = []
        for i in range(len(freq)-1, -1, -1):
            res.extend(freq[i])
            if len(res) >= k:
                break
        
        return res