"""
Monotonic Stack algorithm for Next Greater Element computation.
"""
def next_greater_elements(nums: list) -> list:
    res = [-1] * len(nums)
    stack = []
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            idx = stack.pop()
            res[idx] = num
        stack.append(i)
    return res
