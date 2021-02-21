# 第8周学习笔记

## 位运算，布隆过滤器，LRU cache以及排序算法

### 位运算

- 左移  <<  
- 右移  >>  
- 按位或 ︳  
- 按位与 &
- 按位取反  ~
- 按位异或（相同为零不同为一）  ^
- 异或：相同为0，不同为1。也可用“不进位加法”来理解。
  - 异或操作的一些特点：
    - x ^ 0 = x
    - x ^ 1s = ~x  // 注意1s = ~0
    - x ^ (~x) = 1s
    - x ^ x = 0
    - c = a ^ b   =>   a ^ c = b, b ^ c = a      // 交换两个数
    - a ^ b ^ c = a ^ (b ^ c) = (a ^ b) ^ c     // associative


**指定位置的位运算：**

1.将x 最右边的n 位清零：x& (~0 << n)


3.获取x 的第n 位值（0 或者1）：(x >> n) & 1


5.获取x 的第n 位的幂值：x& (1 <<n)


7.仅将第n 位置为1：x | (1 << n)


9.仅将第n 位置为0：x & (~ (1 << n))


11.将x 最高位至第n 位（含）清零：x& ((1 << n) -1)指定位置的位运算


**实战位运算要点：**

- 判断奇偶：
  - x % 2 == 1  —> (x & 1) == 1
  - x % 2 == 0  —> (x & 1) == 0

- x >> 1 —> x / 2.     
  - 即：x = x / 2;   —>    x = x >> 1;
  - mid = (left + right) / 2;   —>    mid = (left + right) >> 1;

- X = X & (X-1) 清零最低位的1

- X & -X => 得到最低位的1

- X & ~X => 0


### 布隆过滤器

布隆过滤器是一个很长的二进制向量和一系列随机映射函数。布隆过滤器可以用于检索一个元素是否在一个集合中。

布隆过滤器的优点是空间效率和查询时间都远远超过一般的算法

它的缺点是有一点的误识率和删除困难。当布隆过滤器判定一个元素不在一个集合中时，则这个元素一定不在数据库中；但是当布隆过滤器判定一个元素在一个集合中时，则这个元素不一定存在于数据库中。

布隆过滤器的应用：

1）比特币网络

2）分布式系统(Map-Reduce) –– Hadoop, search engine

3) Redis 缓存

4）垃圾邮件，评论等的过滤

**布隆过滤器代码模版**

``` python

from bitarray import bitarray 
import mmh3 

class BloomFilter: 
  
  def __init__(self, size, hash_num): 
    self.size = size 
    self.hash_num = hash_num 
    self.bit_array = bitarray(size) 
    self.bit_array.setall(0) 
    
  def add(self, s): 
    for seed in range(self.hash_num): 
      result = mmh3.hash(s, seed) % self.size 
      self.bit_array[result] =1
      
  deflookup(self, s): 
    for seed in range(self.hash_num): 
      result = mmh3.hash(s, seed) % self.size 
      if self.bit_array[result] ==0: 
        return "Nope"
    return"Probably"
    
 bf = BloomFilter(500000, 7) 
 bf.add("dantezhao") 
 print (bf.lookup("dantezhao")) 
 print (bf.lookup("yyj")) 

```

### LRU cache

LRU cache意思是 Least Recently Used cache，即最近最少使用缓存。

LRU cache的两个要素：大小，元素替换策略(最近最少使用缓存的放到最后去淘汰)

LRU cache 一般通过 哈希表(Hash Table) 再加 双向链表(Double Linked List) 来实现

LRU cache 的查询复杂度是O(1), 修改和更新的复杂度也是O(1)

**LRU cache 代码模版**

``` python

class LRUCache(object): 
  
  def __init__(self, capacity): 
    self.dic = collections.OrderedDict() 
    self.remain = capacity
    
  def get(self, key): 
    if key not in self.dic: 
      return -1
    v = self.dic.pop(key) 
    self.dic[key] = v   # key as the newest one 
    return v 
      
  def put(self, key, value): 
    if key in self.dic: 
      self.dic.pop(key) 
    else: 
      if self.remain >0: 
        self.remain -=1
      else:   # self.dic is full
        self.dic.popitem(last=False) 
    self.dic[key] = value

```

### 排序算法

- 初级排序-O(**N^2**)
  
  - 1.选择排序（Selection Sort）：每次找最小值，然后放到待排序数组的起始位置。
  
  - 2.插入排序（Insertion Sort）：从前到后逐步构建有序序列；对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
  
  - 3.冒泡排序（Bubble Sort）嵌套循环，每次查看相邻的元素如果逆序，则交换。


- 高级排序-O(**N*LogN**)
  
  - 快速排序（Quick Sort）：数组取标杆pivot，将小元素放pivot左边，大元素放右侧，然后依次对右边和右边的子数组继续快排；以达到整个序列有序。
  
  - 归并排序（Merge Sort）：归并和快排具有相似性，但步骤顺序相反。归并排序：先排序左右子数组，然后合并两个有序子数组；而快排：先调配出左右子数组，然后对于左右子数组进行排序。
    - 1. 把长度为n的输入序列分成两个长度为n/2的子序列；
    - 2. 对这两个子序列分别采用归并排序；
    - 3. 将两个排序好的子序列合并成一个最终的排序序列。

  - 堆排序（Heap Sort）：—堆插入O(**logN**)，取最大/小值O(**1**)
    - 1. 数组元素依次建立小顶堆
    - 2. 依次取堆顶元素，并删除


- 特殊排序-O(**N**)
  
  - 计数排序（Counting Sort）：计数排序要求输入的数据必须是有确定范围的整数。将输入的数据值转化为键存储在额外开辟的数组空间中；然后依次把计数大于1 的填充回原数组
  
  - 桶排序（Bucket Sort）：桶排序(Bucket sort)的工作的原理是假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排）。
  
  - 基数排序（Radix Sort）基数排序是按照低位先排序，然后收集；再按照高位排序，然后再收集；依次类推，直到最高位。有时候有些属性是有优先级顺序的，先按低优先级排序，再按高优先级排序。


**快排代码模版(Java)**

``` java
public static void quickSort(int[]array,int begin,int end) {
  if(end <=begin)return;
  int pivot =partition(array, begin, end);
  quickSort(array, begin, pivot -1);
  quickSort(array, pivot + 1, end); 
}
  
static int partition(int[]a,intbegin,intend) {

  // pivot: 标杆位置，counter: 小于pivot的元素的个数
  int pivot =end, counter =begin;
  for(int i=begin; i< end; i++) {
    if(a[i] < a[pivot]) {
      int temp =a[counter]; a[counter]=a[i]; a[i]=temp;
      counter++;
    }
  }
  int temp =a[pivot]; a[pivot]=a[counter]; a[counter]=temp;
  return counter;
} //调用方式：quickSort(a, 0, a.length-1)

``` 
