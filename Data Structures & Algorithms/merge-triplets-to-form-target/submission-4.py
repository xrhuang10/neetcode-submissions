class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first, second, third = target[0], target[1], target[2]

        hashmap = {0:[], 1:[], 2:[]}

        for triplet in triplets.copy():
            if triplet[0] > first or triplet[1] > second or triplet[2] > third:
                triplets.remove(triplet)
            else:
                hashmap[0].append(triplet[0])
                hashmap[1].append(triplet[1])
                hashmap[2].append(triplet[2])
        print(hashmap)
        return first in hashmap[0] and second in hashmap[1] and third in hashmap[2]

        


