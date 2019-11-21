# Quick Sort


num1 = [10, 80, 40, 30, 90, 50, 70]


def division(nums, first, last):
    pivot = nums[last]
    k = first - 1

    for i in range(first, last):
        if nums[i] <= pivot:
            k += 1
            nums[k], nums[i] = nums[i], nums[k]

    nums[k + 1], nums[last] = nums[last], nums[k + 1]
    return k + 1


def quick_sort(nums, first, last):
    if first < last:
        piv_index = division(nums, first, last)

        quick_sort(nums, first, piv_index - 1)
        quick_sort(nums, piv_index + 1, last)


quick_sort(num1, 0, len(num1) - 1)
print(num1)


# Merge Sort

def merge(lis, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    left = [0] * n1
    right = [0] * n2

    for i in range(0, n1):
        left[i] = lis[l + i]

    for j in range(0, n2):
        right[j] = lis[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            lis[k] = left[i]
            i += 1
        else:
            lis[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        lis[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        lis[k] = right[j]
        j += 1
        k += 1


def merge_sort(lis, l, r):
    if l < r:
        m = (l + r - 1) // 2

        merge_sort(lis, l, m)
        merge_sort(lis, m + 1, r)
        merge(lis, l, m, r)


lis = [1, 12, 14, 13, 5, 19, 7, 43]
n = len(lis)

merge_sort(lis, 0, n - 1)
print(lis)


# Insertion Sort

def insertion_sort(lis):
    for i in range(1, len(lis)):

        key = lis[i]
        j = i - 1
        while j >= 0 and key < lis[j]:
            lis[j + 1] = lis[j]
            j -= 1
        lis[j + 1] = key


lis = [1, 12, 11, 13, 5, 23]
insertion_sort(lis)
print(lis)
