# 第4周学习笔记

## DFS(深度优先搜索)和BFS(广度优先搜索)，贪心算法，以及二分查找



### DFS(深度优先搜索)和BFS(广度优先搜索)

**DFS - 递归写法模版**
``` python
visited = set()
def dfs(node, visited):
    visited.add(node)
    
    # process current node here.
    ...
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)
```

**DFS - 非递归写法模版**
``` python
def dfs(self, tree): 
    if tree.root is None: 
        return[] 
    
    visited, stack =[], [tree.root]
    
    while stack: 
        node =stack.pop() 
        visited.add(node)
        
        process (node) 
        nodes = generate_related_nodes(node) 
        stack.push(nodes) 
        
    # other processing work 
    ...
    
```


**BFS 代码模版**
``` python
def BFS(graph, start, end):
    
    queue = []
    queue.append([start])
    visited.add(start)
    
    while queue:
        node = queue.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)
        
    # process other work
    ...
```




### 贪心算法

贪心算法是一种在每一步选择中都采取在当前状态下最好或最优（即最有利）的选择，从而希望导致结果是全局最好或最优的算法。

贪心算法与动态规划的不同在于：它对每个子问题的解决方案都做出选择，不能回退。动态规划则会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。

贪心法可以解决一些最优化问题，如：求图中的最小生成树、求哈夫曼编码等。然而对于工程和生活中的问题，贪心法一般不能得到我们所要求的答案。因为贪心法只局部选择最优解，当前选择对后续不产生影响。

**贪心算法基本思路：**

- 建立数学模型来描述问题

- 分解为若干子问题

- 依序对每一个子问题求最优解(下一个包含上一个的最优解)

- 把所有子问题的局部最优解合并为原问题的一个解




### 二分查找

**二分查找的前提：**

- 目标函数单调性（单调递增或者递减） 

- 存在上下界（bounded） 

- 能够通过索引访问（index accessible)




**二分查找代码模版**
``` python
left, right =0, len(array) -1
while left <= right:   
    mid = left + (right - left) / 2 
    
    if array[mid] == target:
        # find the target!!  
        break or return result  
        
     elif array[mid] < target:      
        left = mid +1
        
     else:      
        right = mid -1
```




