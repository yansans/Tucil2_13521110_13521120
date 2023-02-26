from point import *

def merge_sort(points: list, n: int) -> list:
    if len(points) <= 1:
        return points

    mid = len(points) // 2
    left = merge_sort(points[:mid], n)
    right = merge_sort(points[mid:], n)

    return merge(left, right, n)


def merge(left: list, right: list, n: int) -> list:
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i].c[n] <= right[j].c[n]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


def quicksort(points: list, n : int) -> list:
    if len(points) <= 1:
        return points

    pivot = points[len(points) // 2]
    
    left = [p for p in points if p.c[n] < pivot.c[n]]
    middle = [p for p in points if p.c[n] == pivot.c[n]]
    right = [p for p in points if p.c[n] > pivot.c[n]]
    
    return quicksort(left, n) + middle + quicksort(right, n)