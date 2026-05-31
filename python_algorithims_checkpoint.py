# 1. Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

print("1. Binary Search")
print(binary_search([1, 2, 3, 5, 8], 6))
print(binary_search([1, 2, 3, 5, 8], 5))


# 2. Power Function
def power(a, b):
    result = 1
    for i in range(b):
        result *= a
    return result

print("\n2. Power Function")
print(power(3, 4))


# 3. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print("\n3. Bubble Sort")
print(bubble_sort([29, 13, 22, 37, 52, 49, 46, 71, 56]))


# 4. Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

print("\n4. Merge Sort")
print(merge_sort([29, 13, 22, 37, 52, 49, 46, 71, 56]))


# 5. Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left  = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

print("\n5. Quick Sort")
print(quick_sort([29, 13, 22, 37, 52, 49, 46, 71, 56]))