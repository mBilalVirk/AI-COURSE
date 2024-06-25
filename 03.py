# Applying different function on the list
list0=[]
list1=['one','two','three','four']
list2=['1','2','3','4']
list3=[[1,2],[3,4]]
list4=[1,'alex', 12,1.5]
print(len(list1))

list1.append('five')
print(list1)

list1.insert(2,'three')
print("\n")
print(list1)
print("\n")
list1.remove('four')
print(list1)
print("\n")
list1.append(list4)
print(list1)
print("\n")
list2.extend(list4)
print(list2)
print("\n")
del (list4[0])
# list4.
print(list4)

list6=['5d','6','8','9','7']
list6.reverse()
print(list6)
numbers=[73,92,20,38,82,77,43]
sorted_list=sorted(numbers)
print(sorted_list)
list7=['one','two','three','four','usman','ali', 'hello world']
sort_string=sorted(list7)
print(sort_string)
print("reverse sorted list", sorted(list7, reverse=True))
list8="one,two,three,four,five"
spl=list8.split(',')
print(spl)
list9="A lab is being conducted"
spl1=list9.split()
print(spl1)

list10=[98,98,67,88,77,46,21]
# list10[start:stop:step]
print(list10[:])
print(list10[:4])
print(list10[4:])
print(list10[2:6])
print(list10[::6])
print(list10[::2])
print(list10[2::2])
list11=[1,2,3,4]
list12=['alex','john','harry']
list13=list12+list11
print(list13)

list12[0],list12[2]=list12[2],list12[0]
print(list12)

sumList11=sum(list11)
print(sumList11)


import statistics
meanList11=statistics.mean(list11)
print(meanList11)
medianList11=statistics.median(list11)
print(medianList11)
newList=[]
for num in list11:
    square=num*num
    newList.append(square)

print(newList)
cube=0
newList1=[]
for num in list11:
    cube=num*num*num
    newList.append(cube)
print(newList1)

find=int(input("Enter any number that you find in the list"))
for num in list11:
    if num == find:
        print("found")
    else:
        print("not found")
    

