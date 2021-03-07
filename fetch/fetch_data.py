import os
import csv
from fetch.hamiltonwatch import fetch_hamiltonwatch
from fetch.tissotwatches import fetch_tissotwatches
from fetch.longines import fetch_longines
from config import log



def fetch(site: str, article: str) -> dict:
    ''' Description: fetch data for site
        Input: site
        Output: data about products

    '''
    log.info('Fetching site is ' + site)
    data = {}
    if site == 'hamiltonwatch':
        data = fetch_hamiltonwatch(article)
    elif site == 'tissotwatches':
        data = fetch_tissotwatches(article)
    elif site == 'longines':
        data = fetch_longines(article)
    return data


def write(site: str) -> None:
    ''' Description: writes data to a file for return
        Input: fetch site
        Output: None

    '''
    len_output = os.path.getsize(
        'fetch/output/output_{}.csv'.format(site))
    headers = False
    if len_output == 0:
        headers = True
    with open('fetch/input/input_{}.csv'.format(site), 'r', encoding='utf-8') as csvinput:
        with open('fetch/output/output_{}.csv'.format(site), 'a', encoding='utf-8') as csvoutput:
            reader = csv.reader(csvinput)
            for row in reader:
                log.debug('Row in input file is ' + row)
                if row[0] != 'article':
                    data = fetch(site, row[0])
                    writer = csv.DictWriter(csvoutput, fieldnames=data)
                    if headers:
                        headers = False
                        writer.writeheader()
                    writer.writerow(data)
