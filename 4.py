def transform_and_remove_duplicates(nums):
    unique_nums = list(set(nums))

    if len(nums) % 2 != 0:
        unique_nums.append(nums[-1])

    for i in range(0, len(unique_nums) - 1, 2):
        unique_nums[i], unique_nums[i + 1] = unique_nums[i + 1], unique_nums[i]

    return unique_nums


nums = [1, 2, 3, 3, 4, 5, 6]
result = transform_and_remove_duplicates(nums)
print(result)
