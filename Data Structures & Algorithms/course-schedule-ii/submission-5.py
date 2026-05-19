class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        seen = set()
        res = []

        adj = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        def dfs(course):
            if course in seen:
                return False
            
            if adj[course] == []:
                if course not in res:
                    res.append(course)
                return True

            
            seen.add(course)

            for prereq in adj[course]:
                if dfs(prereq) == False:
                    return False
            
            res.append(course)
                    
            
            seen.remove(course)
            adj[course] = []
            
            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return []
        
        for i in range(numCourses):
            if i not in res:
                res.append(i)
        
        return res