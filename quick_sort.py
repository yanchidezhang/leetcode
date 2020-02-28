# approach 1 start
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [value for value in arr if value < pivot]
    middle = [value for value in arr if value == pivot]
    right = [value for value in arr if value > pivot]

    return quickSort(left) + middle + quickSort(right)
# approach 1 end

# approach 2 start
def quick_sort(array, l, r):
    if l < r:
        # q is the index of the pivot
        q = partition(array, l, r)
        # using the new pivot to divide the array
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)


def partition(array, l, r):
    pivot = array[r]
    i = l - 1

    for j in range(l, r):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


arr = [77, 25, 32, 7, 4, 79]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
# approach 2 end
