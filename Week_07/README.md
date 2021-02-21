# 第7周学习笔记

## 字典树和并查集，高级搜索，以及AVL树和红黑树



### 字典树

字典树，即 Trie 树，又称单词查找树或键树，是一种树形结构。典型应用是用于统计和排序大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。 

字典树的优点是：最大限度地减少无谓的字符串比较，查询效率比哈希表高。

Trie 树的核心思想是空间换时间。 利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的。

**字典树的基本性质：**

- 结点本身不存完整单词； 


- 从根结点到某一结点，路径上经过的字符连接起来，为该结点对应的字符串； 


- 每个结点的所有子结点路径代表的字符都不相同


**Trie 树代码模版 (Python)**
``` python
class Trie(object):
  
    def __init__(self):
        self.root = {}
        self.end_of_word = "#"
        
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node
        
    def startsWith(self, prefix):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return True
```



### 并查集

并查集是一种树型的数据结构，用于处理一些不相交集合（Disjoint Sets）的合并及查询问题，例如组团和配对问题。

**并查集的基本操作：**
- makeSet(s)：建立一个新的并查集，其中包含 s 个单元素集合。 


- unionSet(x, y)：把元素 x 和元素 y 所在的集合合并，要求 x 和 y 所在的集合不相交，如果相交则不合并。 


- find(x)：找到元素 x 所在的集合的代表，该操作也可以用于判断两个元素是否位于同一个集合，只要将它们各自的代表比较一下就可以了。基本操作

**并查集(Disjoint Set)代码模版 (Python)**
``` python
  def init(p):  
    # for i = 0 .. n: 
    p[i] = i;  p = [i for i in range(n)]  
    
  def union(self, p, i, j):   
    p1 = self.parent(p, i)   
    p2 = self.parent(p, j)   
    p[p1] = p2  
    
  def parent(self, p, i):   
    root = i  
    
    while p[root] != root:    
      root = p[root]      
    while p[i] != i: # 路径压缩 
      x = i; i = p[i]; p[x] = root 
    
    return root

``` 



### 高级搜索

初级搜索：

- 1.朴素搜索 

- 2.优化方式：不重复（fibonacci）、剪枝（生成括号问题） 

- 3.搜索方向： 
  - DFS: depth first search 深度优先搜索 
  - BFS: breadth first search 广度优先搜索 
  
  - 双向搜索、启发式搜索

**常用的几种高级搜索：**
- 1.剪枝
  - 剪枝是指通过某些判断，避免一些不必要的遍历过程，形象的说，就是减去搜索树的某些枝条。应用剪枝优化的核心问题是设计剪枝判断方法，即确定哪些枝条舍弃哪些枝条保留。
  - 剪枝的优化技巧：
    - 1.优化搜索顺序
    - 2.排除等效冗余
    - 3.可行性剪枝
    - 4.最优性剪枝


- 2.双向BFS
  - 很多时候，双向BFS的队列底层数据结构会用set，特别是那种左边动一步，右边动一步，每次就把所有一层的节点处理完，生成新的一层的节点的情况，用set能更好的判断对面的节点是否也在当前的节点里有。


- 3.启发式搜索(A*)
  - 启发式搜索（Heuristic Search, A*），Heuristic指的是根据某一些条件，我们不断的优化搜索方向，本质上用的就是利用优先级进行查找。
  - 启发式搜索的核心在定义估价函数h(n)，h(n)用来评价哪些结点最有希望的是一个我们要找的结点，h(n) 会返回一个非负实数，也可以认为是从结点n的目标结点路径的估计成本。 
  - 启发式函数是一种告知搜索方向的方法。它提供了一种明智的方法来猜测哪个邻居结点会导向一个目标。 

**双向BFS的代码模版：**
``` python
  def dBFS(graph, start, end):
    visited = set()
    front = []
    back = []
    
    front.append(start)
    back.append(end)
    
    while front and back:
        nodes = set()
        for node in front:
            visited.add(node) #加入访问
            process(node) # 处理当前node
            nodes.append(generate_related_nodes(node)) #获取子节点
        
        front = nodes
        # 从较小的set开始
        if len(back) < len(front):
            front, back = back, front
   ...
        
``` 

**启发式搜索(A star Search)的代码模版：**
``` python
  def AstarSearch(graph, start, end):

    pq = collections.priority_queue() # 优先级 —> 估价函数
    pq.append([start]) 
    visited.add(start)

    while pq: 
        node = pq.pop() # can we add more intelligence here ?
        visited.add(node)

        process(node) 
        nodes = generate_related_nodes(node) 
         unvisited = [node for node in nodes if node not in visited]
        pq.push(unvisited)
``` 

### AVL树

AVL树的特点：
- 1.AVL树是平衡二叉搜索树


- 2.每个结点存平衡因子(Balance Factor)，平衡因子是它的左子树的高度减去它的右子树的高度（有时相反）。Balance Factor = {-1, 0, 1}


- 3.通过四种旋转操作来进行平衡:
  - 左旋
  - 右旋
  - 左右旋
  - 右左旋


*AVL树的不足*：结点需要存储额外信息、且调整次数频繁





### 红黑树

红黑树是一种近似平衡的二叉搜索树（BinarySearch Tree），它能够确保任何一个结点的左右子树的高度差小于两倍。

红黑树是满足如下条件的二叉搜索树：
- 每个结点要么是红色，要么是黑色

- 根结点是黑色

- 每个叶结点（NIL结点，空结点）是黑色的。

- 不能有相邻接的两个红色结点

- 从任一结点到其每个叶子的所有路径都包含相同数目的黑色结点。


*红黑树的关键性质*：从根到叶子的最长的可能路径不多于最短的可能路径的两倍长。


### AVL树与红黑树的对比：

- AVL树比红黑树查询效率更快

- 红黑树比AVL树的插入和删除操作效率更快

- AVL树比红黑树需要更多的存储空间，因为AVL树需要额外存储平衡因子

- 大多数程序语言的映射map和集合set是由红黑树实现的；而AVL树多用于数据库的实现中，因为AVL树有更快的查询检索效率

