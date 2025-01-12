class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        sorted_heights = sorted(heights)
        
        count = 0
        
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                count += 1
                
        return count


#https://leetcode.com/problems/height-checker/