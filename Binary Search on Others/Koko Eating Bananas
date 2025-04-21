class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        
        # Initialize two pointers
        # Left to 1
        # Right to the max value of the piles array
        # Since k cannot be more than that
        l = 1
        r = max(piles)
        # Let the result also be same as r
        res = max(piles)

        # While left is less than right
        while l <= r:
            # Find the middle point of the l and r
            k = (l + r) // 2
            # Let the hours variable be initialized to 0
            hours = 0
            
            # Iterate through all values in piles
            for p in piles:
                # Calculate the total hours required for each value of p
                hours = hours + math.ceil(float(p)/float(k))

            # If the total hours is less than h
            if hours <= h:
                # Update res
                res = min(res, k)
                # Update r since we do not need to look to the right of r
                r = k - 1
            else:
                # Update l since we do not need to look to the left of r
                l = k + 1
        # Return res
        return res
