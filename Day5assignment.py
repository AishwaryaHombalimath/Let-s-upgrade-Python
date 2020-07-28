#Sort the given list in ascending order but all zeros must be at the end

list1= [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
list1.sort()
k=list1.count(0);
print(list1[k:]+list1[:k])

#o/p :-[1, 1, 1, 2, 2, 3, 4, 4, 10, 56, 56, 0, 0, 0, 0, 0]

#Merge two given sorted lists and create one sorted list

l1 = [10,20,40,60,70,80]
l2 = [5,15,25,35,45,60]
Lst =l1+l2
ResList=[]
for i in range(min(Lst),max(Lst)+1):
    if i in Lst:
        ResList.append(i)
print(ResList)

#o/p :-[5, 10, 15, 20, 25, 35, 40, 45, 60, 70, 80]
