import csv
import sys
 
def portofolio_cost(filepath):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    total_cost = 0
    with open(filepath) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            z = zip(headers, row)
            print(z)
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares*price
            except TypeError:
                print(f"Row {rowno}: Bad row {row}")
        
    return total_cost


if __name__ == "__main__":

    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = print("Enter the path to the portofolio")

    print(portofolio_cost(filename))

