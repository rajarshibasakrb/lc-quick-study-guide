class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Initialize dict for storing count of all characters
        count = {}
        
        # Initialize variable for storing result
        result = 0
        
        # Left pointer
        l = 0
        
        # Using the right pointer as the iterator
        for r in range(len(s)):
            # Update the count dict
            count[s[r]] = count.get(s[r], 0) + 1
            print("Printing s[r]: ", s[r], count[s[r]])
            
            # Check if len(window) - count of max value from dictionary
            # is more than k (allowed value)
            while (r - l + 1) - max(count.values()) > k:
                # decrease count of character in dict
                count[s[l]] -= 1
                print("Printing s[l]: ", s[l], count[s[l]])
                # Move l pointer to the right
                l += 1
                
            # Update result to be max of result and len(window) 
            result = max(result, r - l + 1)
            print(result)
            
        return result
