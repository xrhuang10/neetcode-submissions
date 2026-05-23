class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hashmap = {}
        for i in range(len(hand)):
            hashmap[hand[i]] = 1 + hashmap.get(hand[i], 0)

        minHeap = list(hashmap.keys())
        heapq.heapify(minHeap)
        while hashmap:
            min_key = minHeap[0]
            for key in range(min_key, groupSize + min_key):
                if key not in hashmap:
                    return False
                
                hashmap[key] -= 1
                if hashmap[key] == 0:
                    del hashmap[key]
                    heapq.heappop(minHeap)
        
        
        return True
            