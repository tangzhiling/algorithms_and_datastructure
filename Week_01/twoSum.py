#ID: G20200343080282
#Name: Zhiling Tang
#Class:21
#Language: Python
#Link of homework: 
#Link of Notes:

def twoSum(nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""

		values = dict()

		for index, elem in enumerate(nums):
			complement_num = target - elem

			if complement_num in values:
				return [values[complement_num], index]

			values[elem] = index

		return None


print "Enter the given list:"
mylist = input()
print "Enter the target value:"
mytarget = input()

myresult = twoSum(mylist, mytarget)
print myresult

