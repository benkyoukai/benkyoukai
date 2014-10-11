def merge_sort(nums, cmp=cmp):
    length = len(nums)
    if length < 2:
        return nums

    left_length = length / 2
    right_length = length - length / 2
    left = merge_sort(nums[0: left_length], cmp)
    right = merge_sort(nums[left_length:], cmp)
    merged = []

    i, j = 0, 0
    while True:
        if i == left_length:
            merged.extend(right[j:])
            break

        if j == right_length:
            merged.extend(left[i:])
            break

        if cmp(left[i], right[j]) < 0:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    return merged

if __name__ == "__main__":
    # test
    import random

    for i in range(10):
        size = random.randrange(100)
        t1 = random.sample(xrange(100), size)
        assert merge_sort(t1) == sorted(t1)

    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]

    print "=> passed"
