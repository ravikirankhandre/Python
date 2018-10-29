#Unorderdered collection,Unique values
#can apply on list,tuple,dictionary

SL=[1,2,3,4,2,3]
ST=('a','b','ac')
SD={1:2,2:3,3:4}
print('set of list:',set(SL))
print('set of tuple:',set(ST))
print('set of dict:',set(SD))
print(set("RAVIKIRAN"))

###Methods

#Union
s1=[1,2,3,4]
s2=[1,5,6]
print("union:",set(s1).union(set(s2)))
#Difference
print("Difference:",set(s1).difference(set(s2)))
#Intersection
print("Intersection:",set(s1).intersection(set(s2)))
#symmetric_difference
print("symmetric_difference:",set(s1).symmetric_difference(set(s2)))
#update
s11=set([1,2,3,4])
s22=set([1,5,6])
s11.update(s22)
print("update:",s11)
#difference_update
s11=set([1,2,3,4])
s22=set([1,5,6])
s11.difference_update(s22)
print("difference_update:",s11)
#symmetric_difference_update
s11=set([1,2,3,4])
s22=set([1,5,6])
s11.symmetric_difference_update(s22)
print("symmetric_difference_update:",s11)
#add
s22=set([1,5,6])
s22.add(5)
print(s22)
s22.add(8)
print(s22)
#remove
s22.remove(5)
print(s22)
#discard
s22.discard(5)
print(s22) #remove will give error if element not .
#pop
s22.pop()
print(s22)
#issubset
s1=set([1,2,3])
s2=set([1,2,3,4,5])
s3=set([1,2,6,7,8])
print(s1.issubset(s2))
print(s1.issubset(s3))
print(s3.issubset(s1))
#issuperset
s1=set([1,2,3])
s2=set([1,2,3,4,5])
print(s1.issuperset(s2))
print(s2.issuperset(s1))

