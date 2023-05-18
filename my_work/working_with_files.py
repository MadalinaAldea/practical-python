import os

os.getcwd()

#Read csv data

with open("Work\Data\portfolio.csv") as f:
    data = f.read()
    
print(data)

with open("Work\Data\portfolio.csv") as f:
    for line in f:
        print(line)

f = open("Work\Data\portfolio.csv", "rt")
headers = next(f)
print(headers)
f.close()