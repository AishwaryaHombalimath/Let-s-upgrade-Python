# 1) Use dictionary, p1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}
# and make new dictionary in which keys become values and values become keys
#as : p2 = {“FTP":21, "SSH":22, “telnet":23,"http": 80}

p1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}
x1=list(port1.keys())
x2=list(port1.values())
p2={  x2[i]:x1[i]  for i in range(len(x1)) }
print(p2) 

#o/p :- {“FTP":21, "SSH":22, “telnet":23,"http": 80}

# 2) Take a list as shown below [(1,2,3), [1,2], ['a','hit','less']] 
#The List contains tuple and lists. Make the elements of inner lists 
#and tuples to outer list

list1=[(1,2,3),[1,2],['a','hit','less']]
res=[]
for i in list1: 
    if type(i)==type(list1): 
        res=res+i
    elif type(i)==tuple:
        res.extend(i)
    else: 
        res.append(i)

print(res)

#o/p:- [1, 2, 3, 1, 2, 'a', 'hit', 'less']

# 3) Take a list of tuple as below:-
[(1,2), (3,4), (5,6),(4,5)]
Make a new list which contains sum of number of tuples

list2=[(1,2),(3,4),(5,6),(4,5)]
res=[ sum(i)  for i in list2]
print(res)
#o/p:-[3, 7, 11, 9]
