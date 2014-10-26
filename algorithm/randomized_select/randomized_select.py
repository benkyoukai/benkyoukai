import random



def randomized_select(array, index, cmp=cmp):
    """ select the nth smallest element """
    # input array should be duplicated first.
    return rselect(list(array), index, cmp)


def rselect(array, index, cmp=cmp):
    def select_between(start, end):
        def pivot_index():
            """ return pivot index """
            return random.randint(start, end)

        def partition():
            """
            partition an array
            given some array with first element as pivot
            it will rearrange this array in the following order:

                < pivot | pivot | >= pivot

            return the pivot's final index
            """
            i = start
            pivot = array[start]

            for j in range(start, end + 1):
                if cmp(array[j], pivot) < 0:
                    i += 1
                    swap(i, j)

            swap(start, i)
            return i

        def swap(i, j):
            """ swap two elements by index """
            array[i], array[j] = array[j], array[i]

        # Not found
        if start < 0 or start > end: return

        # choose a pivot, get its index
        pi = pivot_index()
        # make the first element as pivot
        swap(pi, start)
        # partiioning
        mid = partition()

        # Found the element.
        if mid == index: return array[index]
        # search in right hand side
        elif mid < index: return select_between(mid + 1, end)
        # search in left hand side
        else: return select_between(start, mid - 1)

    return select_between(0, len(array) - 1)

if __name__ == "__main__":

    expected = list(range(0, 100))
    for i in range(1, 100):
        t = list(expected)
        index = random.randint(0, 99)
        assert randomized_select(t, index) == index

    assert randomized_select(list(expected), 100) is None

    print "=> passed"
