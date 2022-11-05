# https://blog.teclado.com/destructuring-in-python/
# standard destructuring
x, y = 5, 11
print(x,y)

# destructure a tuple
m,n = (6,7)
print(m,n)

# 'enumerate' an iterable object is also an example of destructuring

# ignoring values

person = ('bob', 42, "programmer") 

name, _, profession = person
print(name, profession)

# when we don't care any of the values in a range loop
for _ in range(5):
    print("ok")

''' using * to collect values
In Python, we can use the * operator to collect leftover values when 
performing a destructuring assignment.
we can also use 'pop' in this example
'''

head, *tail = [1, 2, 3, 4, 5]

print(head)  # 1
print(tail)  # [2, 3, 4, 5]

# the other way around
*head, tail = [1, 2, 3, 4, 5]

print(head)  # [1, 2, 3, 4]
print(tail)  # 5

'''more usage of *'''
head, *middle, tail = [1, 2, 3, 4, 5]

print(head)    # 1
print(middle)  # [2, 3, 4]
print(tail)    # 5