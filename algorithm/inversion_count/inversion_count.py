def isort(nums, cmp=cmp):
    length = len(nums)
    if length < 2:
        return nums, 0

    left_length  = length / 2
    right_length = length - length / 2
    left, left_count = isort(nums[0: left_length], cmp)
    right, right_count = isort(nums[left_length:], cmp)
    count = 0
    merged = []

    i, j = 0, 0
    while True:
        if i == left_length:
            merged.extend(right[j:])
            break

        if j == right_length:
            merged.extend(left[i:])
            break

        if cmp(left[i], right[j]) <= 0:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            count += left_length - i
            j += 1

    return merged, left_count + count + right_count

def inversion_count(nums, cmp=cmp):
    _, count = isort(nums, cmp)
    return count

if __name__ == "__main__":
    quit("WARNING: No tests for function inversion_sort")
