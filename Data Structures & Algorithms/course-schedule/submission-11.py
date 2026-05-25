class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        def dfs(course, seen):
            if adj[course] == []:
                return True

            if course in seen:
                return False

            seen.add(course)

            for nei in adj[course]:
                if dfs(nei, seen) == False:
                    return False
            adj[course] = [] #processed
    

        for course in range(numCourses):
            seen = set()
            if dfs(course, seen) == False:
                return False
        
        return True
                
            
