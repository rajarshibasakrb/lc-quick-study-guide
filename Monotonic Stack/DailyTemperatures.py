class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        # My solution (Not efficient)  
        result = []

        stack = []

        for i in range(len(temperatures)):
            j = i + 1
            while (j < len(temperatures)) and (temperatures[j] <= temperatures[i]):
                stack.append(temperatures[j])
                j += 1
            if j >= len(temperatures):
                result.append(0)
            else:
                result.append(len(stack)+1)
            del stack[:]

        return result

        #--------------------------------------------------------------------------#

        # Efficient Solution
        # Initialize the result array
        result = [0] * len(temperatures)

        stack = []

        # Iterate through all temperatures and indices from array
        for i, t in enumerate(temperatures):
            # As long as the stack is not empty and ith temp is more than 
            # the first element in the stack
            while len(stack) != 0 and t > stack[-1][0]:
                # Remove the first element from the stack
                stackTemp, stackIndex = stack.pop()
                # Update the result array
                result[stackIndex] = (i - stackIndex)
                print(result)
            # Add the new element to the end of the stack
            stack.append([t, i])
            print("The stack is: ", stack)
        # Return the result array
        return result
