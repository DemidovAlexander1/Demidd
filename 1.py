def find_majority_element(nums):
    for num in nums:
        if nums.count(num) > len(nums) / 2:
            return num
    return 0


nums = [1, 6, 6, 6, 7, 7, 7, 7, 7]
result = find_majority_element(nums)
print(result)
