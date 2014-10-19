def qsort(array, cmp=cmp):
    """ Quick sort """

    def sort(start, end):
        def pivot_index():
            """ return pivot index """
            return start

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
            t = array[i]
            array[i] = array[j]
            array[j] = t

        # Base case.
        if start < 0 or start >= end: return

        # choose a pivot, get its index
        pi = pivot_index()
        # make the first element as pivot
        swap(pi, start)
        # partiioning
        mid = partition()

        # sort the left hand side
        sort(start, mid - 1)
        # sort the right hand side
        sort(mid + 1, end)

    sort(0, len(array) - 1)
    return array


if __name__ == "__main__":
    import random

    expected = list(range(0, 100))
    for i in range(1, 100):
        t = list(expected)
        random.shuffle(t)
        assert qsort(t) == expected, t

    print "=> passed"
