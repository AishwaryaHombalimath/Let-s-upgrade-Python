#Program to find index of substring in a string
str1=str1="What we think we become,we are python programmers "
str1.find("we")
#op:5
str1.rfind("we")
#op:24
str1.index("we",6,30)
#op:14
for index, char in enumerate(str1):
   print("", char, "-->", index)
#op: W --> 0
 h --> 1
 a --> 2
 t --> 3
   --> 4
 w --> 5
 e --> 6
   --> 7
 t --> 8
 h --> 9
 i --> 10
 n --> 11
 k --> 12
   --> 13
 w --> 14
 e --> 15
   --> 16
 b --> 17
 e --> 18
 c --> 19
 o --> 20
 m --> 21
 e --> 22
 , --> 23
 w --> 24
 e --> 25
   --> 26
 a --> 27
 r --> 28
 e --> 29
   --> 30
 p --> 31
 y --> 32
 t --> 33
 h --> 34
 o --> 35
 n --> 36
   --> 37
 p --> 38
 r --> 39
 o --> 40
 g --> 41
 r --> 42
 a --> 43
 m --> 44
 m --> 45
 e --> 46
 r --> 47
 s --> 48
   --> 49

#Program to check islower() and isupper() 
a="heaven"
a.islower() 
#op-true
a.isupper() 
#op-false

b="HELL"
b.isupper()
#op-true
b.islower() 
#op-false

c="God"
c.isupper() 
#op-false
c.islower() 
#op-false

