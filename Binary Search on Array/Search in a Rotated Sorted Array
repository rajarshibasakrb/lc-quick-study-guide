class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            
            mid = (left + right)//2

            if target == nums[mid]:
                return mid

            # Now check which portion of the sorted array we are in
            # Left Sorted Portion
            if nums[left] < nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            # Right Sorted Portion
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1
