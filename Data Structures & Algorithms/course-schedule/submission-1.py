class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        seen = set()
        adj = defaultdict(list)

        adj = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].append(prereq)


        
        print(adj)
        
        def dfs(course):
            if course in seen:
                return False

            if adj[course] == []:
                return True
            
            seen.add(course)

            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            
            seen.remove(course)
            adj[course] = []
            return True


        for course in prerequisites:
            if dfs(course[0]) == False:
                return False
        
        return True
