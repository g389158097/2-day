names=['old_drivers','rain','jack','shanshan','peiqi','black_girl']
names.insert(5,'alex')
names[3]='珊珊'
names.insert(2,['old_boy','old_girl'])
print(names.index('peiqi'))
L1=[1,2,3,4,2,5,6,2]
names.extend(L1)
for i in names:
    a=names.index(i)
    if a%2==0:
      print(-1,i)
    else:
      print(a,i)
#enumerate 枚举 可以直接打出索引值
