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

- 表示算法的速度--算法运行时间（**操作数**）的增速
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

## D&C——分而治之

------

简要描述

- 一种著名的递归式问题解决方法

原理

1. 寻找**简单的**的基线条件
2. 确定如何缩小问题的规模，使其符合基线条件

## 快速排序

------

简要描述：

- 快速排序是一种常用的排序算法，比选择排序快得多

条件：

- 基线条件：数组为空或只包含一个元素
- 递归条件：

步骤：

1.选择基准值(pivot)
2.将数组分成两个子数组：小于基准值的元素和大于基准值的元素（分区）
3.对这两个子数组进行快速排序

## 归纳证明

------

简要描述

- 与D&C协同发挥作用

## 散列表

------

简要描述

- 一种结合散列函数和数组的数据结构
- 包含额外逻辑的数据结构

**p.s.** 散列表在python中的实现为字典

应用案例

1. 模拟映射关系
2. 防止重复
3. 缓存/记住数据

### 散列函数

------

简要描述

- 将输入映射到数字

要求

- 映射结果必须一致
- 将不同输入映射到不同的数字（索引）


### 冲突

------

简要描述

- 散列表给两个键分配的位置相同

### 性能

------

简要描述

- 避免冲突

操作

1. 较低的装填因子——调整长度（在散列表中添加位置）
2. 良好的散列函数——让数组中的值呈均匀分布

#### 装填因子

------

简要描述

$$
\cfrac{散列表包含的元素数}{位置总数}
$$

**p.s.** 当装填因子大于0.7时，需要调整散列表的长度

## 图

简要描述

- 模拟一组连接
- 由节点和边组成

类别

1. 有向图——节点的关系是单向的
2. 无向图——直项链的节点互为邻居

## 广度优先搜索

简要描述

- 是一种用于图的查找算法

操作

- 在广度优先搜索的执行过程中，搜索范围从起点开始逐渐向外延伸，即先检查一度关系，再检查二度关系

**p.s.** 检查前要确认是非检查过该元素，避免无限循环

运算时间

$$
O(V + E)
$$

V为顶点数，E为边数

代码实现

```python
from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person+ ' is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search('you')
```

## 队列

简要描述

- 队列是一种先进先出（First In First Out，FIFO）的数据结构，而栈是一种后进先出（Last In First Out，LIFO）的数据结构

创建队列(python)

```python
from collections import deque
search_queue = deque()
search_queue += graph['you']
```

