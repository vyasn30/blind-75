class Solution:
    def twoSum(self, nums, target: int):
        # My solution
        for index, value in enumerate(nums):
            difference = target - value
            if difference in nums:
                if index != nums.index(difference):
                    return [index, nums.index(difference)]

             
        # Neet's solution:
        # prevMap = {}  # val -> index

        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in prevMap:
        #         return [prevMap[diff], i]
        #     prevMap[n] = i


            
if __name__ == "__main__":
    nums = [3,2,3]
    target = 6
    print(Solution().twoSum(nums, target))
