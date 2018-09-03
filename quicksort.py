def quicksort(array):
    """快速排序"""

    if len(array) < 2:
        # 基线条件
        return array
    else:
        # 递归条件
        pivot = array[0]
        # array可能有重复的元素，所以需要小于或者等于
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)
