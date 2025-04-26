class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Initialize a dictionary to store course as key,
        # and list of prerequisites as list of values
        preMap = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        # Initialize a set to look for loops
        visitSet = set()

        # Define recursive dfs
        def dfs(course):
            # All the base cases
            if course in visitSet:
                return False # Since there is a loop
            if preMap[course] == []:
                return True # Since the course has no prerequisites

            # Add course to visitSet
            visitSet.add(course)

            # Go through each prerequisite in course
            for prereq in preMap[course]:
                # If dfs returns False (there is a loop), return False
                if dfs(prereq) == False:
                    return False
            # Remove the course from the visitSet as we are done 
            # visiting this course
            visitSet.remove(course)
            # Set preMap for that course to empty list
            # as the course's prerequisites can be completed 
            preMap[course] = []
            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return False
        return True
