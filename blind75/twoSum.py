def twoSum(self, nums: List[int], target: int) -> List[int]:
    num_indices = {}
    for i, num in enumerate(nums):
        rem = target - num
        if rem in num_indices:
            return [num_indices[rem], i]
        elif num not in num_indices:
            num_indices[num] = i