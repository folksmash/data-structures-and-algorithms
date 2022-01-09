# Merge Sort

## Pseudo Code

ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left


### Solution

    ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

This step sets up the area to work in by establishing a variable to give our array a size (length)

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side

When we sort the array we have to start somewhere. This method will use a /2 or dividing by 2 solution to pick a middle. This scales with any size array. After the array is scaled left it will repeat the process on the right side to give us the full size of the array.

      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

With each side of the array defined we can now call the Mergsort function to sort both left and right together. Finally Merge is used to create our sorted array



ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1

The Merge function takes in the pre sorted left and right side of the array as arguments. Additionally you will interate through the length of both left and right sides to place them in the new array

        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left

To complete the function if the right side completes a mirror action of the left. This checks the length of both left and right arguments to confirm the middle placement of both.
