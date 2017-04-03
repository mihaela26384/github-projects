fruit_list = ["bananas", "cherries", "oranges", "lemons", "pineapples", "apples", "pears", "sour cherries"]
my_iterator = iter(fruit_list)
for item in range(0, len(fruit_list)):
    print(next(my_iterator))

o = range(0, 100, 4)
print(o)
p = o[::5]
print(p)
for i in p:
    print(i)