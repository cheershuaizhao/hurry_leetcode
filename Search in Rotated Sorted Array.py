'''
find the target is in which side of sequence by comparing the target with the last element.
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return -1
        
        l, r = 0, len(nums) - 1
        if target == nums[0]:
            return 0
        if target == nums[-1]:
            return len(nums) - 1
        
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if target < nums[-1]:
                if nums[mid] > nums[-1] or nums[mid] < target:
                    l = mid
                else:
                    r = mid
            else:
                if nums[mid] < nums[-1] or nums[mid] > target:
                    r = mid
                else:
                    l = mid
                    
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1
