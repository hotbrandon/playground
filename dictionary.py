from loguru import logger

logger.info('dictionary keys must be hashable, e.g., int, str, float')
a = { 1:'brandon', 2:'jack', 3:'david' }
print('content of dict "a"')
print(a)
print('keys of dict "a"')
print(a.keys())
print('values of dict "a"')
print(a.values())
print('items in dict "a"')
print(a.items())
logger.info('dictionary comprehension is a method for transforming one dict into another')

logger.info('general pattern for dictionary comprehension')
print('==> { k:v for (k,v) in a.items()}')
b = { k:v + ' huang' for (k,v) in a.items()}
print(b)

logger.info('keys can also be changed')
c = { k*10:v for (k,v) in a.items()}
print(c)

logger.info('solving the same problem with a for loop or dictionary comprehension')
numbers = range(10)

# for loop example
dict_for = {}
for x in numbers:
    if x%2 == 0:
        dict_for[x] = x*x
print(dict_for)

# dictionary comprehension example
dict_comprehension = {n:n*n for n in numbers if n%2 == 0}
print(dict_comprehension)


logger.info('convert celsius to fahrenheit')
cel = {'t1':30, 't2':40, 't3':50}
fa = {k:v/5*9+32 for (k,v) in cel.items()}
print(fa)