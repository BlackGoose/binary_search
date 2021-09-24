def binary_search(numbers: list, target: int) -> int:
    first = 0
    end = len(numbers) - 1

    while first <= end:
        average = (first + end)//2
        if numbers[average] == target:
            return average

        if numbers[average] > target:
            end = average - 1
        else:
            first = average + 1

    return None
