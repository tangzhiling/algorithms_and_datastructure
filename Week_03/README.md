# 第3周学习笔记

## 泛型递归和树的递归，分治，回溯

### 泛型递归和树的递归

递归本质上是循环，它是通过函数体来进行的循环。需要运用数学归纳法的思维，找到最近最简方法，将其拆解成可重复解决的问题（重复子问题）。


**递归代码模版**

``` python
def recursion(level, param1, param2, ...):
  
  # recursion terminator
  if level > MAX_LEVEL:
      print_result
      return
      
   # process logic in current level
   process_data(level, data...)
   
   # drill down
   self.recursion(level+1, p1, ...)
   
   # reverse the current level status if needed
   reverse_state(level)

```

树的面试题的解法一般都是用递归，例如二叉树的前序、中序和后序遍历就是通过递归来实现的。


### 分治



**分治代码模版**

``` python
def divide_conquer(problem, param1, param2, ...)
    #recursion terminator
    if problem is None:
        print_result
        return
        
    # prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)
    
    # conquer subproblems
    subresult1 = self.divide_conquer(subproblems[0], p1, ...)
    subresult2 = self.divide_conquer(subproblems[1], p1, ...)
    subresult3 = self.divide_conquer(subproblems[2], p1, ...)
    ...
    
    # process and generate the final result
    result = process_result(subresult1, subresult2, subresult3, ...)
    
    # revert the current level states
```

### 回溯

回溯法采用试错的思想，它尝试分步的去解决一个问题。在分步解决问题的过程中，当它通过尝试发现现有的分步答案不能得到有效的正确的解答的时候，它将取消上一步甚至是上几步的计算，再通过其它的可能的分步解答再次尝试寻找问题的答案。 

回溯法通常用最简单的递归方法来实现，在反复重复上述的步骤后可能出现两种情况： 

- 找到一个可能存在的正确的答案； 
- 在尝试了所有可能的分步方法后宣告该问题没有答案。 

在最坏的情况下，回溯法会导致一次复杂度为指数时间的计算。

**回溯法代码模版**
``` python
res = []    # 定义全局变量保存最终结果
state = []  # 定义状态变量保存当前状态
p,q,r       # 定义条件变量（一般条件变量就是题目直接给的参数）

def backtracking(状态，条件1，条件2，……):
    if # 不满足合法条件（可以说是剪枝）
        return
    elif # 状态满足最终要求
        res.append(state)   # 加入结果
        return 
    
    # 主要递归过程，一般是带有 循环体 或者 条件体
    for # 满足执行条件
    if  # 满足执行条件
        backtracking(状态，条件1，条件2，……)
back(状态，条件1，条件2，……)
return res

```

**使用回溯法的明显标志**

- 排列、组合（子集、幂集、字符全排列）。 在传值时，对于排列问题，是要删掉单个用过的元素；组合问题，是删掉前面所有的元素。


- 数组、字符串，给定一个特定的规则，尝试搜索迭代找到某个解。


- 二维数组下的DFS搜索（八皇后、黄金矿工、数独）
