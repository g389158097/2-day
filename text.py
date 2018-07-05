#数据类型 列表
#方便数据的存储
#[]是列表的标志
#列表内部也可以嵌套列表
#方法一[]
#方法二list（）
L1=['a','b','c','d','e']
print(L1[0])
print(L1.index('a'))
#创建  查询  index count
#切片  顾头不顾尾
a=L1[1:-1]
print(a)
#隔一个取一个  调整步长
b=L1[::2]
print(b)
#增加新值 append
L1.append('f')
print(L1)
L1.insert(2,'abd')
print(L1)
#修改  直接index赋值
L1[2]='2'
print(L1)
#连续修改用切片
L1[:2]=['q','w','e']
print(L1)
#删除  pop remove
L1.pop()
print(L1)
L1.remove('q')
print(L1)
#del 全局性删除指令，不光删除列表  del可以批量删除
del L1[1]
print(L1)
#循环  for 循环
for i in range(10):
    print(i)
#for跟while的区别
#for不可能为死循环，有边界



#排序 sort
del L1[1]
print(L1.sorted())
#reverse 倒转列表
#列表相加n.extend(n2)
#clear删除    copy拷贝
#对于列表来讲，一个列表由另一个列表赋值而来，一个改变了，另一个也改变了
#与变量不一样，而copy的作用就是避免这种错误。
