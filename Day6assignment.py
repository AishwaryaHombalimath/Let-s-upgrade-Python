#Create a dictionary using Comprehension method

list1=[1,2,3,4,5,6,7,8]
list2=['a','b','c','d','e']
dict1={}
dict1={ list1[i]:list2[i]  for i in range(min(len(list1),len(list2))) }
print(dict1) 

#o/p:- {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
