from collections import Counter, defaultdict

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

total_shares = Counter()
holdings = defaultdict(list)
for name, shares, price in portfolio:
    total_shares[name] += shares
    holdings[name].append((shares, price))

print(total_shares['GOOG'])
print(holdings['IBM'])

