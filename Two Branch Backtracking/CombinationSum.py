class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Initialize array to store result
        result = []

        def dfs(i, current, total):
            # Cover all the base cases
            if total == target:
                result.append(current.copy())
                return
            if total > target or i >= len(candidates):
                return

            # Add the ith value from the candidates array
            current.append(candidates[i])
            # Call dfs recursively with i, current array, and
            # total incremented by value at ith position in candidates array 
            # i.e. (next larger value)
            # This is the left child of the tree
            dfs(i, current, total + candidates[i])
            print("Current array before popping: ", current)
            current.pop()
            print("Current array after popping: ", current)
            # Call dfs recursively with incremented index, current array, and
            # same value as before (total)
            # This is the right child of the tree
            dfs(i+1, current, total)

        # Call dfs for the root of the tree
        dfs(0, [], 0)
        return result
