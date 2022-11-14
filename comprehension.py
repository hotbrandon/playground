# list comprehension is an easier and more readable way to create lists
list1 = [1, 2, 3, 4, 5]

list2 = []
for i in list1:
    list2.append(i*i)
print(list2)

# with list comprehension
list3 = [n*n for n in list1]

print(list3)

# with map function
list4 = list(map(lambda n: n*n, list1))

print(list4)
