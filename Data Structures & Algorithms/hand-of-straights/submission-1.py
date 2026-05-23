class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hashmap = {}
        for i in range(len(hand)):
            hashmap[hand[i]] = 1 + hashmap.get(hand[i], 0)

        
        min_keys = sorted(hashmap.keys())
        for minimum in min_keys:
            if minimum in hashmap:
                count = hashmap[minimum]
                for num in range(minimum, groupSize + minimum):
                    
                    if hashmap.get(num, 0) < count:
                        return False
                    
                    hashmap[num] -= count
                    if hashmap[num] == 0:
                        del hashmap[num]
        
        return True
            