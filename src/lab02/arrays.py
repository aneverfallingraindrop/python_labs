def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        return(ValueError)
    return(tuple(min(nums), max(nums)))

print(min_max([42]))
