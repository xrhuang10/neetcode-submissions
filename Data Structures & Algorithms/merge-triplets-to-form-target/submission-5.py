class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first, second, third = target[0], target[1], target[2]
        a, b, c = 0, 0, 0

        for triplet in triplets:
            if triplet[0] <= first and triplet[1] <= second and triplet[2] <= third:
                a = max(a, triplet[0])
                b = max(b, triplet[1])
                c = max(c, triplet[2])
        
        if a == first and b == second and c == third:
            return True
        return False


        


