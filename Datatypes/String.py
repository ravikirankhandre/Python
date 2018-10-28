fname='Ravikiran'
lname='Khandre'
print('first name:',fname,'lname:',lname)

print('fname:%s lname:%s'%(fname,lname))

print(type(fname))

print('fname : {} lname: {} '.format(fname,lname))

#STRING FUNCTIONS

#1.CENTER

print('Center Method:  ',fname,fname.center(20,'@'))

#2.COUNT

print('Count Method(a): ',fname,fname.count('a'))

#3.CAPITALIZE

print('capitalize Method: ',fname,fname.capitalize())

#4.startswith

print('startswith method: ',fname.startswith('kiran',4))
print('startswith method: ',fname.startswith('Ravi',0))

#5.endswith

print('endswith method: ',fname.endswith('kiran',4))
print('endswith method: ',fname.endswith('Ravi',0))

#6.expandtabs : default tab contain 8 spaces
str='I am Ravi\tKiran'
print('Expandtabs: ',str,str.expandtabs(16))

#7.find --if not found return -1 else index
str1='i am ravikiran'
str2='kiran'
print(str1.find(str2,0))
print(str1.find('kha',0))

print(str1.rfind('ravi',0))

#8.index  --if not found error else index

print(str1,str2,str1.index(str2,0))
#print(str1.index('kha',0))

#9.ljust rjust --rjust means name at right

print(fname,fname.ljust(15,'*'),fname.rjust(15,'#'))

#10.strip --remove spaces
str='       thanks  a lot  '
print(str,'\'',str.strip(),'\'')
str1='%%ravikiran%%'
print(str1,str1.rstrip('%'))

#11.title --upper,lowe,swapcase

str='This is string program'
print(str,str.title())

#12.isalnum, isdigit , isnumeric , isdecimal , isalpha ,islower , isupper , isspace , istitle

#13. min max