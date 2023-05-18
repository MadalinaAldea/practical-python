import csv

types = [str, int, float]
f = open('Work/Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
first_row = next(rows)
print(first_row)

types = [str, float, str, str, float, float, float, float, int]
converted = [func(val) for func, val in zip(types, first_row)]
record = dict(zip(headers, converted))
print(record)

# print(f'total price of holdings for first row is {first_row[1]*first_row[2]}')