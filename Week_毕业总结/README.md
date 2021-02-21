# 毕业总结

十周的训练营已经结束，我总体的体验是收获很多。算法和数据结构这门课本就是是我本科和研究生时期非常喜欢的一门课，但毕业后由于自己的工作写的大多是业务代码和一些后台维护，对于曾经的这些知识点已经忘记了很多，通过这个训练营跟着覃超老师有效地重拾了大多数知识点，也从实践上锻炼了自己对这些知识点的理解和代码实现能力，感觉很充实很开心。

对于整个训练营的知识点，我个人印象比较深刻，也是花时间最多的是这几个：**动态规划**，**递归**和**分治算法**，**深度优先**和**广度优先搜索**，**二分查找**，**排序算法**和**Trie树**。在没有上这个训练营之前我没有背代码模版的意识，但现在我意识到熟练的记住和灵活运用这些常用的代码模版对解决面试题也好，或者在工作中写工程代码也好都有极大的帮助。

以下列出对我个人而言受益最多的几个方面：

## 常用的代码模版

### 动态规划代码模版 
``` java
// 状态定义
dp = new int [m+1][n+1];

// 初始状态
dp[0][0] = x;
dp[0][1] = y;
...

// DP状态推导
for i = 0; i <= n; ++i {
    for j = 0; j <= m; ++j {
        ...
        
        d[i][j] = min{dp[i-1][j], dp[i][j-1], etc};  
    }
}

return dp[m][n]; // 最优解

```


### 递归代码模版 
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

### 分治代码模版 
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


### DFS - 递归写法模版 
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

### BFS 代码模版 
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



### 二分查找代码模版 
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



### Merge sort 代码模版 
``` java
public static void mergeSort(int[] array,int left,int right) {
  
  if(right <=left)  return;
  int mid =(left + right) >> 1; // (left + right) / 2
  
  mergeSort(array,left,mid);
  mergeSort(array,mid + 1,right);
  merge(array,left,mid,right);
}

public static void merge(int[] arr, int left, int mid, int right) {

    int[] temp = new int[right - left + 1]; 
    int i = left, j = mid + 1, k = 0;
    
    while (i <= mid && j <= right) {
        temp[k++] = arr[i] <= arr[j] ? arr[i++] : arr[j++];
    }
    
    while (i <= mid) temp[k++] = arr[i++];
    while (j <= right) temp[k++] = arr[j++];
    
    for (int p = 0; p < temp.length; p++) {
        arr[left + p] = temp[p];
    }
}

```

### Trie 树代码模版 (Python)
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

##  切题四件套
- 1）Classification: 明确题目意思，边界，数据规模等

- 2）Possible solutions: 穷尽所有可能的解法
  -  compare time/space 比较时间和空间复杂度
  -  optimal solution 找出最优解
        
- 3）Coding

- 4）Test cases

## 五毒神掌 （五步刷题法）
- 1）第一遍：5分钟读题加思考，若5分钟内没有思路，则直接看解法，比较题解中各种解法的优劣，背诵并默写好的解法

- 2）第二遍：自己写并在leetcode上提交，多种解法进行比较，体会区别并优化
        
- 3）第三遍：24小时后再重复做题，练习不同解法的熟练程度

- 4）第四遍：一周后反复回来练习以前做过的相同题目

- 5）第五遍：面试前一周恢复性训练

## 最后
非常感谢覃超老师，班班和助教以及所有为训练营准备和付出心血的工作人员们。

完成了训练营只是一个开始，接下来要提升和巩固自己的能力一个字就是要练，两个字就是要多练。

希望自己在提升综合实力之后，最终能换工作拿到满意的Offer。

