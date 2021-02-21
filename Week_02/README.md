# 第2周学习笔记

## 哈希表、映射、集合；树、二叉树、二叉搜索树；以及堆和二叉堆、图

### 哈希表、映射、集合

哈希表（Hash table），也叫散列表，是根据关键码值（Key value）而直接进行访问的数据结构。它通过把关键码值映射到表中一个位置来访问记录，以加快查找的速度。

哈希表的工程实践有：

- 电话号码簿

- 用户信息表

- 缓存（LRUCache）

- 键值对存储（Redis）

在平均情况下，哈希表的查询、插入和删除的实践复杂度均为O(**1**)，而在最差的情况下哈希表的查询、插入和删除的实践复杂度均为O(**N**)


### 树、二叉树、二叉搜索树

**树的代码模版(Python)**
```python

classTreeNode: 
  def __init__(self, val): 
    self.val = val 
    self.left, self.right =None, None
```

**二叉树遍历Pre-order/In-order/Post-order**

- 前序遍历（Pre-order）：根-左-右

- 中序遍历（In-order）：左-根-右

- 后序遍历（Post-order）：左-右-根

**二叉树遍历代码模版(Python)**
```python
  def preorder(self, root): 
    if root: 
      self.traverse_path.append(root.val) 
      self.preorder(root.left) 
      self.preorder(root.right)
      
  def inorder(self, root):
    if root: 
      self.inorder(root.left) 
      self.traverse_path.append(root.val) 
      self.inorder(root.right)
      
  def postorder(self, root):
    if root: 
      self.postorder(root.left) 
      self.postorder(root.right) 
      self.traverse_path.append(root.val)
```      
      
**二叉搜索树 Binary Search Tree**

二叉搜索树，也称二叉排序树、有序二叉树（OrderedBinary Tree）、排序二叉树（SortedBinary Tree），是指一棵空树或者具有下列性质的二叉树：
- 1. 左子树上所有结点的值均小于它的根结点的值；
- 2. 右子树上所有结点的值均大于它的根结点的值；
- 3. 以此类推：左、右子树也分别为二叉查找树。

二叉搜索树的中序遍历是升序排列。在平均情况下，二叉搜索树的查询、插入和删除的实践复杂度均为O(**log(N)**)，而在最差的情况下二叉搜索树的查询、插入和删除的实践复杂度均为O(**N**)


### 堆和二叉堆

堆(Heap)是一种可以迅速找到一堆数中的最大者或者最小者的数据结构。将根结点最大的堆叫大顶堆，根结点最小的堆叫小顶堆。常见的堆有二叉堆、斐波那契堆等。

假设一个堆为大顶堆，常见操作的时间复杂度为：

find-max: O(**1**)
delete-max: O(**log(N)**)
insert(create): O(**log(N)**) or O(**1**)

**二叉堆的性质**

- 通过完全二叉堆来实现(不是完全二叉搜索树)
- 二叉堆(大顶堆)满足下列性质：
  - 1）是一棵完全树
  - 2）树中任何节点的值总是大于或等于其子节点的值

**二叉堆实现细节**：

假设二叉堆的第一个元素在数组中的索引为0的话：

- 根结点是 a[0]
- 索引为i的左孩子的索引为(2*i + 1)
- 索引为i的右孩子的索引为(2*i + 2)
- 索引为i的父亲节点的索引为floor( (i-1)/2 )














