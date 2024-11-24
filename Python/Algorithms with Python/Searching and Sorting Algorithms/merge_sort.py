def merge_arrays(left, right):
    merged_array = [None] * (len(left) + len(right))
    left_idx = 0
    right_idx = 0
    result_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged_array[result_idx] = left[left_idx]
            left_idx += 1
        else:
            merged_array[result_idx] = right[right_idx]
            right_idx += 1
        result_idx += 1

    while left_idx < len(left):
        merged_array[result_idx] = left[left_idx]
        left_idx += 1
        result_idx += 1

    while right_idx < len(right):
        merged_array[result_idx] = right[right_idx]
        right_idx += 1
        result_idx += 1

    return merged_array


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid_idx = len(nums) // 2
    left_sub = nums[:mid_idx]
    right_sub = nums[mid_idx:]

    sorted_left = merge_sort(left_sub)
    sorted_right = merge_sort(right_sub)

    return merge_arrays(sorted_left, sorted_right)


nums = [int(x) for x in input().split()]
sorted_nums = merge_sort(nums)
print(*sorted_nums, sep=' ')
