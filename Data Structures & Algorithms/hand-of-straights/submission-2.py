class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hashmap = {}
        for i in range(len(hand)):
            hashmap[hand[i]] = 1 + hashmap.get(hand[i], 0)

        while hashmap:
            min_key = min(sorted(hashmap.keys()))
            for key in range(min_key, groupSize + min_key):
                if key not in hashmap:
                    return False
                
                hashmap[key] -= 1
                if hashmap[key] == 0:
                    del hashmap[key]
        
        
        return True
            