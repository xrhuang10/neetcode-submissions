class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first, second, third = [], [], []
        a, b, c = 0, 0, 0
        for triplet in triplets.copy():

            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                a = max(a, triplet[0])
                b = max(b, triplet[1])
                c = max(c, triplet[2])

        return a == target[0] and b == target[1] and c == target[2]


        


