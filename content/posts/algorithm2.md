+++
date = '2026-06-25T15:07:11+08:00'
draft = false
title = '算法记录'
tags = ['']
lastmod = '2026-06-25T15:07:11+08:00'
+++

### Leetcode：两数相加

#### 题目描述
给出两个按位存储非负整数的链表（低位在前），将对应位相加，产生进位时向更高位进 1，返回相加后的链表。

```go
type ListNode struct {
    Val  int
    Next *ListNode
}

// 示例实现（保留原示例逻辑，仅规范代码块和缩进）
func twoListNodeSum(l1, l2 *ListNode) (head *ListNode) {
    var tail *ListNode
    carry := 0

    for l1 != nil || l2 != nil {
        n1, n2 := 0, 0
        if l1 != nil {
            n1 = l1.Val
            l1 = l1.Next
        }
        if l2 != nil {
            n2 = l2.Val
            l2 = l2.Next
        }

        sum := n1 + n2 + carry
        sum, carry = sum%10, sum/10

        if head == nil {
            head = &ListNode{Val: sum}
            tail = head
        } else {
            tail.Next = &ListNode{Val: sum}
            tail = tail.Next
        }
    }
    if carry > 0 && tail != nil {
        tail.Next = &ListNode{Val: carry}
    }
    return
}
```

### 双指针

双指针是处理有序数组或链表时常用的技巧。常见类型包括：相向指针（两端往中间）、同向指针（快慢指针）、分离指针（分别遍历不同数组/链表）。下面示例展示常见用法。

示例：用双指针求两个数组的交集（先排序再线性扫描）

```python
def find_common_element(arr1, arr2):
    a = sorted(arr1)
    b = sorted(arr2)
    i = j = 0
    common = []
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            if not common or a[i] != common[-1]:
                common.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return common
```

#### Golang 中的双指针示例

两数之和（有序数组）——利用左右指针，时间 O(n)

```go
import (
    "fmt"
    "sort"
)

func twoEle(numbers []int, target int) []int {
    left, right := 0, len(numbers)-1
    for left < right {
        sum := numbers[left] + numbers[right]
        if sum == target {
            return []int{left + 1, right + 1}
        } else if sum < target {
            left++
        } else {
            right--
        }
    }
    return []int{}
}

func main() {
    numbers := []int{2, 11, 7, 15}
    target := 9
    sort.Ints(numbers)
    fmt.Println(twoEle(numbers, target))
}
```

删除有序数组中的重复项（快慢指针示例）

```go
func removeDuplicates(numbers []int) int {
    if len(numbers) == 0 {
        return 0
    }
    slow := 0
    for fast := 1; fast < len(numbers); fast++ {
        if numbers[slow] != numbers[fast] {
            slow++
            numbers[slow] = numbers[fast]
        }
    }
    return slow + 1
}
```

### 贪心算法

贪心算法在每一步都做出局部最优选择，希望得到全局近似或最优解。常见应用有任务调度、区间调度、零钱兑换（在特定币制下）等。

示例：任务分配（Python）

```python
def min_total_execution_time(tasks, n):
    total_time = sum(tasks)
    max_task = max(tasks)
    # 理论下界：不小于最长任务或平均负载上界
    min_possible_T = max(max_task, (total_time + n - 1) // n)

    workers = [0] * n
    for task in sorted(tasks, reverse=True):
        idx = workers.index(min(workers))
        workers[idx] += task
    return max(workers)

tasks = [5, 2, 1, 7, 3, 4]
print(min_total_execution_time(tasks, 3))  # 8
```

```python
def coin_change(coins, amount):
    coins.sort(reverse=True)
    count = 0
    remaining = amount
    for coin in coins:
        if remaining >= coin:
            num = remaining // coin
            count += num
            remaining -= num * coin
        if remaining == 0:
            break
    return count if remaining == 0 else -1

coins = [25, 10, 5, 1]
amount = 37
print(coin_change(coins, amount))
```

```python
# 最多活动数量
def max_activities(activities):
    activities.sort(key=lambda x: x[1])
    count = 1
    last_end = activities[0][1]
    for i in range(1, len(activities)):
        start, end = activities[i]
        if start >= last_end:
            count += 1
            last_end = end
    return count

activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
print(max_activities(activities))
```


### 广度优先搜索（BFS）与深度优先搜索（DFS）
<!-- 示例图：树的三种遍历（请把图片文件放到 `static/images/tree-traversals.png`） -->
<figure>
    <img src="/images/tree-traversals.png" alt="Tree traversals: preorder, inorder, postorder" style="max-width:100%;height:auto;">
    <figcaption>图：树的先序 / 中序 / 后序遍历示意（先序 preorder，中序 inorder，后序 postorder），来源：作者插图。</figcaption>
</figure>

**定义与直观理解**
- 广度优先搜索（BFS）：按层次（离起点距离由近到远）逐层遍历图或树，通常用队列实现。
- 深度优先搜索（DFS）：沿着一条路径尽可能深入后回溯，常用递归或显式栈实现。

**伪代码（图的遍历）**

BFS（伪代码）:

```text
queue = [start]
visited = {start}
while queue:
    node = queue.pop(0)
    for nei in neighbors(node):
        if nei not in visited:
            visited.add(nei)
            queue.append(nei)
```

DFS（递归，伪代码）:

```text
def dfs(node):
    visited.add(node)
    for nei in neighbors(node):
        if nei not in visited:
            dfs(nei)
```

**Python 示例**

```python
from collections import deque

def bfs(graph, start):
    q = deque([start])
    visited = {start}
    order = []
    while q:
        v = q.popleft()
        order.append(v)
        for w in graph.get(v, []):
            if w not in visited:
                visited.add(w)
                q.append(w)
    return order

def dfs(graph, start):
    visited = set()
    order = []
    def _dfs(v):
        visited.add(v)
        order.append(v)
        for w in graph.get(v, []):
            if w not in visited:
                _dfs(w)
    _dfs(start)
    return order

# 简单图示例
g = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}
print('BFS:', bfs(g, 'A'))  # ['A','B','C','D','E']
print('DFS:', dfs(g, 'A'))  # ['A','B','D','C','E']
```

**时间与空间复杂度**
- 时间复杂度（图/树）：O(V + E)
- 空间复杂度：BFS 需要队列保存整层节点，最坏情况 O(V)；DFS 递归栈或显式栈最坏也为 O(V)。

**典型应用场景**
- BFS：用于寻找无权图的最短路径、层次遍历、最小步数问题、最近公共祖先（在树上）等。
- DFS：用于连通性检测、拓扑排序、强连通分量、回溯搜索（如数独、全排列）、树的各种遍历（先/中/后序）。

**为什么 DFS 有先序/中序/后序，而 BFS 没有？**

先序（preorder）、中序（inorder）、后序（postorder）是针对包含“父-子”关系的树结构并基于 DFS（通常递归）的访问顺序定义的：
- 先序：先访问节点，再递归访问左子树、右子树（根左右）。
- 中序：先访问左子树，再访问根，最后右子树（左根右）。中序在二叉搜索树上能得到有序序列，因此有特别含义。
- 后序：先访问左右子树，最后访问根（左右根）。常用于释放/汇总子树信息。

这些序列依赖于“先深入到子树然后回溯”的递归结构，因此属于 DFS 的特性。而 BFS 是按层次广度展开，它在同一层的节点之间并不按照“父-子递归顺序”处理，因此没有“中序/先序/后序”这样基于递归子树的自然定义；BFS 的对应概念是“层序遍历（level order）”。

示例（二叉树）及各遍历结果：

```
    A
   / \
  B   C
 /     \
D       E
```

- 先序（DFS preorder）： A B D C E
- 中序（inorder，仅对二叉树有意义）： B D A C E （取决于左右子树位置）
- 后序（postorder）： D B E C A
- 层序（BFS）： A B C D E

**小结**
- 选择 BFS 还是 DFS，依据问题需要：若求最短路径或层级信息优先选 BFS；若需要枚举解空间、拓扑或深入子问题用 DFS。DFS 的先/中/后序是递归遍历的三种自然输出顺序，而 BFS 则是层序遍历，没有对应的“中序/先序/后序”定义。

