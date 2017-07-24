'''
Created on Apr 21, 2014

@author: varun
'''

import datetime


def main():
    cur_date = datetime.date.today()
    ten_years_ago = cur_date - datetime.timedelta(days = 365 * 10)
    print str(cur_date).replace("-", "/")
    print ten_years_ago

if __name__ == '__main__':
    main()