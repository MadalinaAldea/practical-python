import copy

a = [1, 2, 3]
b = a
print(a is b)

print("Making a copy of a list")
a = [2, 3, [100, 101], 4]
b = list(a)
print(a is b)
print(f' a is {a}, b is {b}')
print(f'a[2] is the same as b[2] because it is a shallow copy, a[2] is b[2]: {a[2] is b[2]}')

print('With copy module you can make a deep copy and then no element is shared')

b = copy.deepcopy(a)

print(" isinstance(a, (list, tuple)) will show is a is instance of list or tuple")