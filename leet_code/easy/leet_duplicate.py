class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        
        

                
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.pop()
                arr.insert(i,0)
                i += 1
            i += 1


#https://leetcode.com/problems/duplicate-zeros/submissions/