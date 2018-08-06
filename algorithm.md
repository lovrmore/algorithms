## 二分查找

------

简要描述：

- 每一次都从中间开始查找

参数：

| 参数名 | 必选 | 类型 | 说明         |
| ------ | ---- | ---- | ------------ |
| list   | 是   | list | **有序列表** |
| item   | 是   | num  | 查找的元素   |

返回示例

> mid
>
> None

返回参数说明

| 参数名 | 类型 | 说明             |
| ------ | ---- | ---------------- |
| mid    | int  | item在列表的位置 |
| None   | bool | 没有找到item     |

代码实现

```python
def binary(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
    
    # Can't not find the item.
    return None
```

## 运行时间

------

大Q表示法

- 表示算法的速度--算法运行时间（操作数）的增速
- 指出了最糟情况下的运行时间

**P.S.** 除最糟情况下的运行时间外，还应考虑平均情况的运行时间

常见的大Q运行时间

- *O* (log *n* )，也叫**对数时间** ，这样的算法包括二分查找
- *O* (*n* )，也叫**线性时间** ，这样的算法包括简单查找
- *O* (*n* * log *n* )，这样的算法包括快速排序——一种速度较快的排序算法
- *O* (*n* 2 )，这样的算法包括选择排序——一种速度较慢的排序算法
- *O* (*n* !)，这样的算法包括接下来将介绍的旅行商问题的解决方案——一种非常慢的算法
- O(1)，常量时间

## 数组和链表

------

- 数组中的元素在内存中相连
- 链表中的元素可储存在内存的任何地方，链表的每个元素都储存了下一个元素的地址

|      | 数组 | 链表 |
| ---- | ---- | ---- |
| 读取 | O(1) | O(n) |
| 插入 | O(n) | O(1) |
| 删除 | O(n) | O(1) |

## 选择排序

-------

简要描述：

- 将数组元素按某种特殊的顺序排序

参数：

| 参数名 | 必选 | 类型 | 说明 |
| ------ | ---- | ---- | ---- |
| arr    | 必选 | list | 列表 |

返回示例

> arr = [5, 3, 6, 2, 10]
> newArr = [2, 3, 5, 6, 10]

返回参数说明

| 参数名 | 类型 | 说明             |
| ------ | ---- | ---------------- |
| newArr | list | 经过排序后的数组 |

代码实现

```python
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
```

```python
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newAee.append(arr.pop(smallest))
    return newArr
```

## 递归

------

简要描述：

- 递归函数调用自己

条件：

- 基线条件
  - 函数不调用自己
- 递归条件
  - 函数调用自己

## 栈

------

简要描述：

- 栈是一种简单的数据结构

操作：

- 压入（插入）
- 弹出（删除并读取）

**P.S.**

- 所有函数调用都进入调用栈