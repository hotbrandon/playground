''' enumerate allows us to create a counter alongside the values
we're iterating over: as part of a loop, for example'''

fruits = ( 'apple', 'banana', 'grape', 'orange')

'''The most common place to find enumerate being used is within 
something like a for loop, with the tuples inside the enumerate 
object destructured into two separate loop variables.
if start is not provided, enumerate begins couting from 0'''
for counter,x in enumerate(fruits, start=1):
    print(counter,x)

'''The use of enumerate is not limited to just for loops, however; 
we can also make use of enumerate as part of a list comprehension, 
for example, or even passed in as an argument to dict'''
friends = ['Johnny', 'Tom', 'Gary']
friends_dict = dict(enumerate(friends))