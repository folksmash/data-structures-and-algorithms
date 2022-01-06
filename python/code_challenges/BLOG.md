# Review the pseudocode below, then trace the algorithm by stepping through the process with the provided sample array. Document your explanation by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.

Pseudocode
  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp

![Whiteboard](/home/folksmash/projects/data-structures-and-algorithms/python/code_challenges/insert_sort.png)

## Efficiency

this solution provides an (O^n) solution if it has to go in reverse order requiring it loop back through itself for however long the array is
this solution is (o-1) spacing due to only needing a temp array to store the data while sorting it.
