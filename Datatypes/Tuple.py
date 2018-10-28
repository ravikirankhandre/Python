#immutable
#()
tup1=(1,4,6)
tup2=2,5,7,'eee','$'
tup3='a',"b","""c"""
print(tup2,type(tup2),list(enumerate(tup2)))
print(tup3,type(tup3))
print(tup3[0:2])
#Methods

#Del : cant delete single element

del tup1
#print(tup1)

#min max
tup4=(1,4,6)
print(max(tup4),min(tup4))

