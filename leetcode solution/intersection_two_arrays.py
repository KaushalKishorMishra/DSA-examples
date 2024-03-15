class Solution(object):
    def __init__(self):
        self.nums3 = []
        self.dist = {}

    def intersection(self, nums1, nums2):
        # for i in nums1:
        #     for j in nums2:
        #         if (i == j) and (i not in self.nums3):
        #             self.nums3.append(i)
        # return self.nums3

        ###### second method
        # for x in nums1:
        #     if x not in self.dist:
        #         self.dist[x] = 0

        # for x in nums2:
        #     if x in self.dist:
        #         self.dist[x] = 1
        # return self.dist
        
        ###### third method
        for num in nums1:
            if num in nums2:
                self.nums3.append(num)
        return set(self.nums3)

    def __str__(self):
        return self.dist


# test cases
sol = Solution()


nums1 = []
n1 = int(input("Enter the size of list for n1:"))
for i in range(n1):
    nums1.append(int(input(f"Enter item {i}: ")))

nums2 = []
n2 = int(input("Enter the size of list for n2:"))
for i in range(n2):
    nums2.append(int(input(f"Enter item {i}: ")))

intersection = sol.intersection(nums1, nums2)

print(intersection)
