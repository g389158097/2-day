cbc_catalog ={
    '小学':{
        '家':['144','155','166'],
        '学校':['花园','456','789'],
        '工作':['55','555']
    },
    '初中':{
        '地点':['新泰','hongwen'],
        '年龄':['cbcb','zzz','zzzz',],
        '同学':['aaa','sss','ddd','eee']
  },
    '高中':{
        '1':['q','w','e'],
        '2':['ee','gg','lol']
    }


}
for k in cbc_catalog:
    print(k,cbc_catalog[k])
cbc_catalog['小学']['学校'][1]+=',happy'
print(cbc_catalog['小学']['学校'])
print(cbc_catalog.keys())
#update 将两个字典合成一个
#item将字典变成一个列表
#setdefault 有值取值没值赋值
#fromkeys批量给key生成值
