from lebara_api import LebaraApi
from tabulate import tabulate
import argparse
import getpass


def main():
    parser = argparse.ArgumentParser(description='lebara cli.')
    parser.add_argument('-u', '--username',
                        dest='username',
                        help='your lebara username',
                        default='')
    parser.add_argument('-p', '--password',
                        dest='password',
                        help='your lebara username',
                        default='')

    args = parser.parse_args()

    if len(args.username) == 0:
        args.username = input('Username: ')
    if len(args.password) == 0:
        args.password = getpass.getpass()

    lebara = LebaraApi(args.username, args.password)
    lebara.login()
    account_summery = lebara.getAccountSummery()
    print(tabulate(account_summery, headers="keys", tablefmt="psql"))
