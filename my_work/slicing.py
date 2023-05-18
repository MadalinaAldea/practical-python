a = [0,1,2,3,4,5,6,7,8]
print(a[2:5]) #LAst value is not included
print(a[-5:])
print(a[:3])

# Deletion
a = [0,1,2,3,4,5,6,7,8]
del a[2:4] 
print(a)

#Break
"""for name in namelist:
    if name == 'Jake':
        break"""
#Continue
"""for line in lines:
    if line == '\n':    # Skip blank lines
        continue"""
print("-------------------------------------------------")
print("Enumerate")
print("-------------------------------------------------")
#Enumerate
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

for index, name in enumerate(names):
    print(index)

print("-------------------------------------------------")
print("Enumerate and list comprehension")
print("-------------------------------------------------")

name_indexes = [ index for index,_ in enumerate(names, start = 1)]
print(name_indexes)

print("-------------------------------------------------")
print("Enumerate examples")
print("-------------------------------------------------")
users = ["Test User", "Real User 1", "Real User 2"]
for index, user in enumerate(users):
    if index == 0:
        print("Extra verbose output for:", user)
    else:
        print(user)

print("-------------------------------------------------")
print("Example 1")
print("-------------------------------------------------")
def even_items(iterable):
    return [i for i, v in enumerate(iterable) if v%2 == 0]

a = [0,1,2,3,4,5,6,7,8]
print(even_items(a))

print("-------------------------------------------------")
print("Example 2")
print("-------------------------------------------------")
values = ["a", "b"]
enum_instance = enumerate(values)
print(next(enum_instance))

def missing_data_rows(filepath):
    with open(filepath) as f:
        for row_number, data in enumerate(f, start=1):
            print(data)
            if data == "\n":
                print(f'Row {row_number} is empty')

missing_data_rows('Work/Data/portfolio.csv')