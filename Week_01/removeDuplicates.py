#ID: G20200343080282
#Name: Zhiling Tang
#Class:21
#Language: Python
#Link of homework: 
#Link of Notes:


from typing import List
class Solution(object):
	def removeDuplicates(self, nums: List[int]) -> int:
		"""
		:type nums: List[int]
		:rtype: int
		"""

		if len(nums) == 0:
			return 0

		prev = None
		ptr = 0

		for elem in nums:
			if elem != prev:
				nums[ptr] = elem
				ptr += 1
				prev = elem

		return ptr
		



mylist = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print ("Enter the given sorted list:", mylist)

print ("The new length of the list after remove duplicates is:", Solution().removeDuplicates(mylist))

