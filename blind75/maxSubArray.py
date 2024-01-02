def maxSubArray(nums: List[int]) -> int:
    global_max = -10**4
    local_max = global_max
    for num in nums:
        local_max = max(num, num + local_max)
        if local_max > global_max:
            global_max = local_max
    
    return global_max