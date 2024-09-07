#String and Numeric values can operate together with *

a=2
b=4
Txt="hi"
print (a*Txt*b)

#String and String can operate with +

a="Hello"
b=3
Txt="hi"
print((a+Txt)*b)

#Numeric values can operate with all arithemetic operators

a=2
b=3
c=4
print(a+b*c)

#Arithematic expression with integer and float will result in float

a=10
b=5.0
c=a*b
print(c)

#Result of division with two integers will be float
a=1
b=2
c=a/b
print(c)

#Integer division with float and int will give int displayed as float
a,b=10.5,2
c=a//b
print(c)

#floor gives closet integer, which is lesser than or equal to the float vaue
#Result of (a//b) is same as floor (a/b)