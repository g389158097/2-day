#字典的用法 字典是一种key-value的数据类型
#语法
info={
       '2013040503031':[24,'cbc'],
       '2013040503032':[23,'wc']
}
print(info['2013040503031'])
#key 必须唯一，可hash 字典不存在索引
#字典无序查找速度快，hash转换为数字可以排序，二分算法
#info.get获取信息 没有信息返回none 不会报错 


#修改 info['2013040503031']='12'
#添加同修改
#删除 del dict['Name']; 删除键是'Name'的条目
#dict.clear();     清空词典所有条目
#del dict ;         删除词典
