class Solution:
    def containsDuplicate(self, nums) -> bool:
        return not len(set(nums)) != len(nums)


if __name__ == "__main__":
    nums = [1,2,3,1]
    print(Solution().containsDuplicate(nums))