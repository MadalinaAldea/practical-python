from collections import Counter
import csv


def count_holdings(filepath):
    holdings = Counter()

    with open(filepath) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            # print(row)
            if len(row) == 0:
                continue
            holdings[row[0]] += int(row[1])
    return holdings


holdings1 = count_holdings('Work/Data/portfolio.csv')
holdings2 = count_holdings('Work/Data/portfolio2.csv')
combined = holdings1 + holdings2
print(combined.elements())
print(holdings1.most_common(2))


data = [("name", 120)]
data = dict(data)
print(data)