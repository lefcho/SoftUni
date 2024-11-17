def recursive_sum(nums, idx):
    if idx == len(nums) - 1:
        return nums[idx]
    return nums[idx] + recursive_sum(nums, idx + 1)


numbers = [int(x) for x in input().split()]

print(recursive_sum(numbers, 0))
