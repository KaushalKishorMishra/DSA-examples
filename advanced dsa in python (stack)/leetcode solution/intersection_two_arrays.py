class Solution(object):
    def __init__(self):
        self.nums3 = []

    def intersection(self, nums1, nums2):
        for i in nums1:
            for j in nums2:
                if (i == j) and (i not in self.nums3):
                    self.nums3.append(i)
        return self.nums3

    def __str__(self):
        return str(self.nums3)


# test cases
sol = Solution()



nums1 = []
n1 = int(input("Enter the size of list for n1:"))
for i in range(n1):
    nums1.append(int(input("Enter the list elements for nums1: ")))
    
nums2 = []
n2 = int(input("Enter the size of list for n2:"))
for i in range(n2):
    nums2.append(int(input("Enter the list elements for nums1: ")))

intersection = sol.intersection(nums1, nums2)

print(intersection)
