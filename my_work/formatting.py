s = {
    'name': 'IBM',
    'shares': 100,
    'price': 91.1
}
p = '{name:>10s} {shares:10d} {price:10.2f}'.format_map(s)
print(p)

name = "IBM"
shares = 100
price = 91.1

print(f'{name:>10s} {shares:^10d} {price:<10f}')
print(b'%s has %d messages' % (b'Dave', 37))
value = 42863.1
print(f'{value:0.4f}')