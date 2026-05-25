class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        seen = set()
        res = []

        adj = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        def dfs(course):
            if adj[course] == []:
                if course not in res:
                    res.append(course)
                return True
            
            if course in seen:
                return False
            
            seen.add(course)

            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
                
            res.append(course)
            adj[course] = []
            
            return True
            
        
        for course in range(numCourses):
            if dfs(course) == False:
                return []
        
        return res
