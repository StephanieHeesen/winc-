# Imports
import argparse
import csv
from datetime import date

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    pass

#start van command line tool
parser = argparse.ArgumentParser(prog= 'superpy', description='Inventory system')
subparser = parser.add_subparsers(dest='command')

# command line to add a bought product.
buy = subparser.add_parser('buy')
buy.add_argument('product_name', type=str, help='name of the product')
buy.add_argument('buy_price', type=float, help='price paid for 1 product')
buy.add_argument('quantity', type=int, help= 'amount of bought products')
buy.add_argument('expiration_date', type=str, help='dat in yyyy-mm-dd when product expired')

# command line to show inventory
inventory = subparser.add_parser('inventory')
inventory.add_argument('time inventory', type=str, help='now or yesterday')

# command line to sell a product.
sell = subparser.add_parser('sell')
sell.add_argument('product_name', type=str, help= 'name of the product')
sell.add_argument('sell_price', type=float, help= 'price for 1 sold product')
sell.add_argument('quantity', type=int, help= 'amount of sold products')

# command line to show sold and expired products.
sold_products = subparser.add_parser('sold_products')

args = parser.parse_args()


#open en show csv files
def all_bought():
    with open('superpy/bought.csv', newline='') as csvfile:
        bought_file = csv.reader(csvfile, delimiter=' ', quotechar=' ')
        for row in bought_file:
            print(' '.join(row))

def all_sold():
    with open('superpy/sold.csv', newline='') as file:
        sold_file = csv.reader(file)
        for row in sold_file:
            print(' '.join(row))


#write csv files
def append_new_product():
    with open('superpy/bought.csv', 'a+', newline='') as write_obj:
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow([id(args.product_name), args.product_name, args.buy_date, args.buy_price, args.expiration_date])
        return 'OK'
            
def sold_product():
    with open('superpy/sold.csv', 'a+', newline='') as write_obj:
        csv_writer = csv.writer(write_obj)
        csv_writer.writerow([args.product_name, args.sell_price, args.quantity])
        return 'OK'

if __name__ == "__main__":
    if args.command == 'inventory':
        print(all_bought())
    elif args.command == 'buy':
        print(append_new_product())
    elif args.command == 'sell':
        print(sold_product())
    elif args.command == 'sold_products':
        print(all_sold())
    main()
