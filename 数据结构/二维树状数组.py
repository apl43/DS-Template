import os,sys,random,threading
#sys.exit() 退出程序
#sys.setrecursionlimit(10**6) #调整栈空间
from random import randint,choice,shuffle
#randint(a,b)从[a,b]范围随机选择一个数
#choice(seq)seq可以是一个列表,元组或字符串,从seq中随机选取一个元素
#shuffle(x)将一个可变的序列x中的元素打乱
from copy import deepcopy
from io import BytesIO,IOBase
from types import GeneratorType
from functools import lru_cache,reduce
#reduce(op,迭代对象)
from bisect import bisect_left,bisect_right
#bisect_left(x) 大于等于x的第一个下标
#bisect_right(x) 大于x的第一个下标
from collections import Counter,defaultdict,deque
from itertools import accumulate,combinations,permutations
#accumulate(a)用a序列生成一个累积迭代器，一般list化前面放个[0]做前缀和用
#combinations(a,k)a序列选k个 组合迭代器
#permutations(a,k)a序列选k个 排列迭代器
from heapq import  heapify,heappop,heappush
#heapify将列表转为堆
from typing import Generic,Iterable,Iterator,TypeVar,Union,List
from string import ascii_lowercase,ascii_uppercase,digits
#小写字母，大写字母，十进制数字
from math import ceil,floor,sqrt,pi,factorial,gcd,log,log10,log2,inf
#ceil向上取整，floor向下取整 ，sqrt开方 ，factorial阶乘
from decimal import Decimal,getcontext
#Decimal(s) 实例化Decimal对象,一般使用字符串
#getcontext().prec=100 修改精度
from sys import stdin, stdout, setrecursionlimit
input = lambda: sys.stdin.readline().rstrip("\r\n")
MI = lambda :map(int,input().split())
li = lambda :list(MI())
ii = lambda :int(input())
mod = int(1e9 + 7) #998244353
inf = 1<<60
py = lambda :print("YES")
pn = lambda :print("NO")
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),(-1, 1)]  # →↘↓↙←↖↑↗

class BIT:
    """二维树状数组 区间加+区间查询 每个操作都是 log(m*n)"""
    #下标从1开始
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
        self.a = [[0]*(col+5) for _ in range(row+5)]
        self.b = [[0]*(col+5) for _ in range(row+5)]
        self.c = [[0]*(col+5) for _ in range(row+5)]
        self.d = [[0]*(col+5) for _ in range(row+5)]

    def _add(self, row: int, col: int, delta: int) -> None:
        i=row
        while i<=self.row:
            j=col
            while j<=self.col:
                self.a[i][j]+=delta
                self.b[i][j]+=delta*row
                self.c[i][j]+=delta*col
                self.d[i][j]+=delta*row*col
                j+=j&-j
            i+=i&-i

    def add(self, row1: int, col1: int, row2: int, col2: int ,delta: int) -> None:
        """矩阵中的点 (row,col) 的值加上delta"""
        self._add(row1,col1,delta)
        self._add(row1,col2+1,-delta)
        self._add(row2+1,col1,-delta)
        self._add(row2+1,col2+1,delta)

    def _query(self, row: int, col: int) -> int:
        res=0
        i=row
        while i>0:
            j=col
            while j>0:
                res+=(row+1)*(col+1)*self.a[i][j]
                res-=        (col+1)*self.b[i][j]
                res-=        (row+1)*self.c[i][j]
                res+=                self.d[i][j]
                j-=j&-j
            i-=i&-i
        return res

    def query(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """查询左上角 (row1,col1) 到右下角 (row2,col2) 的和"""
        res=0
        res+=self._query(row2  ,col2  )
        res-=self._query(row1-1,col2  )
        res-=self._query(row2  ,col1-1)
        res+=self._query(row1-1,col1-1)
        return res

n,m,q=li()

bit=BIT(n,m)

for _ in range(q):
    s=li()
    if s[0]==1:
        a,b,c,d,x=s[1:]
        bit.add(a,b,c,d,x)
    else:
        a,b,c,d=s[1:]
        print(bit.query(a,b,c,d))