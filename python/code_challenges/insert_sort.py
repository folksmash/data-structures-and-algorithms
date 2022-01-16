def insertion_sort(array):
    for i, _ in enumerate(array):
        n = i - 1
        temparray = array[i]

        while n >= 0 and temparray < array[n]:
            array[n+1] = array[n]
            n = n - 1
        array[n+1] = temparray
    return array
