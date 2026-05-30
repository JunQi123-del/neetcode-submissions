class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
                # Step 1: Count frequencies
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # Step 2: Bucket sort — index = frequency
        freq = [[] for _ in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq[cnt].append(num)

        # Step 3: Collect top k from highest frequency buckets
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
            
            
        

        