#!/usr/bin/env python

import argparse
import json
import sys
from datetime import date, datetime, timedelta
from io import StringIO
from pathlib import Path

import pandas as pd
import requests
from colorama import Fore, Style, init
from requests.exceptions import (ConnectionError, HTTPError, RequestException,
                                 Timeout)


TODAY = date.today()
W_URL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"
BASE_DIR = Path(__file__).resolve().parent
DATA = BASE_DIR.joinpath('data.json')

# Console Colors
init()
CYAN = Fore.CYAN
GREEN = Fore.GREEN
RED = Fore.RED
RESET = Style.RESET_ALL


def connect(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/43.0"}  # nopep8
        resp = requests.get(url, timeout=5, headers=headers)
        if resp.status_code != 200:
            sys.exit(f'Failed to get data, Error Code: {resp.status_code}')
        else:
            return resp
    except HTTPError:
        print("HTTP Error:", HTTPError)
    except Timeout:
        print("Timeout encountered:", Timeout)
    except ConnectionError:
        print("Connection Error:", ConnectionError)
    except RequestException:
        sys.exit("Issue encountered:", RequestException)


def get_world(date=None, state=None, country=None, county=None):
    url = f"{W_URL}{TODAY.strftime('%m')}-{date}-{TODAY.year}.csv"
    print(url)
    data = StringIO(connect(url).text)
    pd.set_option('display.max_rows', None)
    with pd.option_context('display.colheader_justify', 'left'):
        columns = [1, 2, 3, 4, 7, 8, 9]
        df = pd.read_csv(data, delimiter=',', usecols=columns, keep_default_na=False)  # nopep8
        if 'Deaths' in df:
            df["Percentage"] = (100. * df['Deaths']/df['Confirmed']).round(2).astype(str) + '%'  # nopep8
            if country:
                df = df.rename(columns={'Admin2': '',
                                        'Province_State': 'Province',
                                        'Country_Region': 'Country'})
                print(f"{CYAN}{country}{RESET}\n{('-' * 25)}")
                country_confirmed = df.loc[df['Country'] == country]
                print(f"Total Confirmed: {country_confirmed['Confirmed'].sum():7,}")  # nopep8
                print(f"Total Deaths: {country_confirmed['Deaths'].sum():9,}")

            if state:
                df = df.rename(columns={'Admin2': 'County',
                                        'Province_State': 'State',
                                        'Country_Region': 'Country'})
                print(df.loc[df['State'] == state].to_string(index=False))
                state_confirmed = df.loc[df['State'] == state]  # nopep8
                print(f"{('-' * 25)}\nTotal Confirmed: {state_confirmed['Confirmed'].sum():7,}")  # nopep8
                print(f"Total Deaths: {state_confirmed['Deaths'].sum():9,}")

            if county:
                df = df.rename(columns={'Admin2': 'County',
                                        'Province_State': 'State',
                                        'Country_Region': 'Country'})
                print(df.loc[df['County'] == county].to_string(index=False))


def main():
    with open(DATA) as json_file:
        JSON_DATA = json.load(json_file)
        
    d_date = datetime.today() - timedelta(days=1)

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-w', '--country',
                       help="Use 2 letter Country")
    group.add_argument('-s', '--state',
                       help="Use 2 letter State")
    group.add_argument('-c', '--county',
                       help="Use 2 letter County")
    parser.add_argument('-d', '--date', default=d_date.strftime("%d"),
                        help="Use 2 digit day, default is minus 1 day")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
        
    if len(args.date) < 2:
        args.date = '0' + args.date

    if args.country:
        try:
            get_world(date=args.date, country=JSON_DATA['countries'][args.country.upper()])  # nopep8
        except KeyError:
            sys.exit(f"{RED}[ERROR]{RESET} The country '{args.country}' was not found.")  # nopep8

    if args.state:
        try:
            get_world(date=args.date, state=JSON_DATA['states'][args.state.upper()])  # nopep8
        except KeyError:
            sys.exit(
                f"{RED}[ERROR]{RESET} The state '{args.state}' was not found.")

    if args.county:
        try:
            get_world(date=args.date, county=args.county.title())  # nopep8
        except KeyError:
            sys.exit(f"{RED}[ERROR]{RESET} The county '{args.county}' was not found.")  # nopep8


if __name__ == "__main__":
    main()
