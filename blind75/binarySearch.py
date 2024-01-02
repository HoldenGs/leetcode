def search(nums: List[int], target: int) -> int:
    i = len(nums) // 2
    if i >= len(nums):
        return -1
    if target == nums[i]:
        return i 
    elif target > nums[i]:
        idx = search(nums[i+1:], target)
        if idx == -1:
            return idx
        else:
            return idx + i + 1
    else:
        return search(nums[:i], target)