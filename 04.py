def sum_list(items):
    sum_numbers =0
    for x in items:
        sum_numbers+=x
    return sum_numbers
print(sum_list([1,2,-8]))

# python program to print
# mean of element


# list of element to calculate mean
n_num = [1,2,3,4,5]
n=len(n_num)

get_sum = sum(n_num)
mean = get_sum / n
print("Mean / Average is: " + str(mean))


# Calculate median of list

# Python program to print
# median of the element
n_num.sort()
if n % 2 == 0:
    median1 = n_num[n//2]
    median2 = n_num[n//2-1]
    median = (median1+median2/2)
else:
    median=n_num[n//2]
print("Median is: " + str(median))

# index function return the very first location where the element is found
t1=(5,6,7,8,9,8,77,99,)
print(t1.index(9))

# Concate tuple
t=(1,2,3,4)
t2=(5,6,7,8)
t3=t+t2
print(t3)

t4=(1,2,3,4,5,6,7,(14,15,16),8,9,10,12,13)

print(t4[:])
print(t4[:4])
print(t4[4:])
print(t4[4::2])


# Sets
# Unordered collection and therefore does not support index
# does not allow duplicates in set.
a={10,20,30,20,40,50}
print(a)
a={1,20,3,40,50}
print(a)

# LOOCV
# leave one out cross validation
# k-fold cross validation
# K Nearest Neighbor classification