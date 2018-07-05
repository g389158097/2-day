products=[['iphone',6888],['macpro',14800],['小米6',2499],['coffee',31],['book',35]]
shop_cart=[]
run_flag=True
while run_flag:
    print('------------welcome shopping------------')
    for index,p in enumerate(products):
        print('%s.%s %s' %(index,p[0],p[1]  ) )
    choice=(input('请输入你所选择的商品编号：'))
    if choice.isdigit():
       choice= int(choice)
       if choice>=0 and choice<len(products):
         shop_cart.append(products[choice])
         print('add %s into your shop cart.'%products[choice])
       else:
           print('商品不存在')

    elif choice=='q':
        if len(shop_cart)>0:
          print('your shopping list is')
          for index,p in enumerate(shop_cart):
              print('%s,%s  %s'%(index,p[0],p[1]))
        else:
            break


        run_flag=False
    else:
         print('your choice is wrong')
         continue

