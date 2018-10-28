#mutable
#{}
#key value pair

dict1 = {1:2,3:5,6:7,'e':33}

print(dict1,type(dict1),id(dict1))

dict2={1:3,2:4}
#Methods
#update
dict1.update(dict2)
print(dict1)
#copy
d1=dict2.copy()
print(d1)
#clear
d1.clear()
print(d1)
#delete
#del dict2
print(dict2)
#keys and values
print('keys: ',dict2.keys(),'values:',dict2.values())
#get value of key
print(dict2.get(2))
#fromkeys
tup=(1,2,3)
abc=dict.fromkeys(tup)
print(abc,type(abc))
#setdefault
