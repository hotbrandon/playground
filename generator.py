# loop without generators
numbers = [1, 2, 3, 4, 5]


def gen_square():
    values = []
    for i in numbers:
        values.append(i*i)
    return values


# values = gen_square()
# print(values)

def generator_demo():
    for i in numbers:
        yield i*i


values = generator_demo()
x = values  # x is a generator
print(x)
print(next(x))

# we can loop through a generator
for y in x:
    print(y)


# normal list comprehension
nums = [x*x for x in [1, 2, 3, 4, 5]]
print(nums)

# list comprehension for generators
nums = (x*x for x in [1, 2, 3, 4, 5])
print("nums is a generator now")
print(nums)
print("you can convert it to a list, but you loose the performance")
print(list(nums))
