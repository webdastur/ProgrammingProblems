# https://leetcode.com/problems/find-target-indices-after-sorting-array/


from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return []
        nums.sort()

        index = nums.index(target)
        result = []

        for i in range(len(nums[index::])):
            if nums[index + i] == target:
                result.append(index + i)
            else:
                break

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.targetIndices([1, 2, 5, 2, 3], 2))
