#mutable
#indexed by integer from 0
#[]

list1 = [1,2,'abc',5]
print(list1,type(list1),id(list1),list(enumerate(list1)))

#List Methods
#append
list1.append(['100',20])
print(list1)
#count
print(list1.count('abc'))
#min max
list2=[1,2,3,4]
print(list1,min(list2),max(list2))
list3=['00abc','rad','xyz','abcd','100']
print(list3,min(list3),max(list3))
#index
print(list2,list2.index(2))
#insert
print(list3.insert(1,'2'),list3)
#pop
list3.pop(1)
print(list3)
#remove
list3.remove('rad')
print(list3)
#reverse
list3.reverse()
print(list3)

#slicing
list4=[1,3,5,4,6,8]
print(list4[-1],list4[1:7],list4[-3:-1])
#sort
print(list4.sort(),list4)