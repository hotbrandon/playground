from loguru import logger

logger.info(
    "list comprehension is an easier and more readable way to create lists")
list1 = [1, 2, 3, 4, 5, 6, 7, 8]

logger.info("loop through a list")
list2 = []
for i in list1:
    list2.append(i*i)
print(list2)

logger.info("simple list comprehension")
list3 = [n*n for n in list1]

print(list3)

logger.info("with map function")
list4 = list(map(lambda n: n*n, list1))

print(list4)

logger.info("list comprehension with conditions")
even_nums = [n*n for n in list1 if n % 2 == 0]
print(even_nums)

logger.info("filter with lambda")
odd_nums = list(filter(lambda n: n % 2 == 1, list1))
print(odd_nums)

logger.info("more complex examples")
num_pairs = [(letter, num) for letter in 'abcd' for num in range(4)]
print(num_pairs)

logger.info("dictionary comprehension")
names = ["bruce wayne", "clark kent", "Peter Parker", "Logan", "Wade"]
heros = ["batman", "superman", "spiderman", "wolverine", "deadpool"]

hero_names = {name: hero for name, hero in zip(
    names, heros) if name != "Peter Parker"}
print(hero_names)
