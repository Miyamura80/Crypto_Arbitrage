
from scrapers.scrape_data import get_data, get_wallet_analytics
import argparse
import os
import sys

# Create the parser
arb_check_parser = argparse.ArgumentParser(description='To help parse through dextools.io')

arb_check_parser.add_argument("-p", "--pair", type=str, metavar='', required=True, help='Pairs Hash. e.g.'\
    'for https://www.dextools.io/app/ether/pair-explorer/0xa29fe6ef9592b5d408cca961d0fb9b1faf497d6d'\
    'use 0xa29fe6ef9592b5d408cca961d0fb9b1faf497d6d')

arb_check_parser.add_argument('-d', '--driver', type=str, metavar='', help='Absolute File path'\
    'of Chrome driver location')

arb_check_parser.add_argument('-s', '--save', type=str, metavar='', help='Save as .xlsx file, with argument as name')

arb_check_parser.add_argument('-w', '--wallet', type=str, metavar='', help='Give analytics of given wallet.'\
    'e.g. profits, overall profit graph, etc')

args = arb_check_parser.parse_args()

if args.save:
    get_data(args.pair, args.save, args.driver)
elif args.wallet:
    get_wallet_analytics(args.pair, args.wallet, args.save, args.driver)
else:
    get_data(args.pair)

