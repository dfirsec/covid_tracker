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

init()

TODAY = date.today()
S_URL = 'https://covidtracking.com/api'
W_URL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"
BASE_DIR = Path(__file__).resolve().parent
DATA = BASE_DIR.joinpath('data.json')

with open(DATA) as json_file:
    JSON_DATA = json.load(json_file)


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


def get_state_info(state=None):
    url = S_URL + f"/states/info?state={state}"
    if connect(url).json():
        info = connect(url).json()
        print(f"\nState Link:\n{info['covid19Site']:<6}\n")
        print(f"Notes:\n{info['notes']:<6}")


def get_states(date=None):
    url = S_URL + f"/states/daily?date={TODAY.year}{TODAY.strftime('%m')}{date}"  # nopep8
    if connect(url).json():
        sp = []  # state positives
        sd = []  # state deaths
        for stats in connect(url).json():
            if 'death' in stats and stats['death'] != 0:
                sp.append(stats['positive'])
                sd.append(stats['death'])
                percent = stats['death'] / stats['positive'] * 100
                print(f"{stats['state']:3} Positive: {stats['positive']:<8,} Deaths: {stats['death']:<6,} {round(percent, 2)}%")  # nopep8
            elif 'death' in stats:
                percent = stats['death'] / stats['positive'] * 100
                if stats['death'] == 0:
                    print(f"{Fore.GREEN}{stats['state']:3} Positive: {stats['positive']:<8,} Deaths: {stats['death']:<6,} {round(percent, 2)}%{Style.RESET_ALL}")  # nopep8
                else:
                    print(f"{stats['state']:3} Positive: {stats['positive']:<8,} Deaths: {stats['death']:<6,} {round(percent, 2)}%")  # nopep8
            else:
                print(f"{Fore.GREEN}{stats['state']:3} Positive: {stats['positive']:<8,} Deaths: 0{Style.RESET_ALL}")  # nopep8

        print(f"\n{Fore.RED}Total: {sum(sp):,} | Deaths: {sum(sd):,} ({round(sum(sd)/sum(sp)*100, 2)}%){Style.RESET_ALL}")  # nopep8


def get_world(date=None, state=None, country=None, county=None):
    url = f"{W_URL}{TODAY.strftime('%m')}-{date}-{TODAY.year}.csv"
    data = StringIO(connect(url).text)
    pd.set_option('display.max_rows', None)
    columns = [1, 2, 3, 4, 7, 8, 9]
    df = pd.read_csv(data, delimiter=',', usecols=columns, keep_default_na=False)  # nopep8
    if 'Deaths' in df:
        df["Percentage"] = (100. * df['Deaths']/df['Confirmed']).round(2).astype(str) + '%'  # nopep8
        if country:
            df = df.rename(columns={'Admin2': ''})
            print(df.loc[df['Country_Region'] == country])
        if county:
            df = df.rename(columns={'Admin2': 'County'})
            print(df.loc[df['County'] == county])
        if state:
            df = df.rename(columns={'Admin2': 'County'})
            print(df.loc[df['Province_State'] == state])


def main():
    d_date = datetime.today() - timedelta(days=1)

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-a', '--all', action='store_true',
                       help="Results for all States")
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

    if args.all:
        get_states(date=args.date)

    if args.country:
        try:
            get_world(date=args.date, country=JSON_DATA['countries'][args.country.upper()])  # nopep8
        except KeyError:
            sys.exit(f"[ERROR] The country '{args.country}' was not found.")

    if args.state:
        try:
            get_world(date=args.date, state=JSON_DATA['states'][args.state.upper()]) # nopep8
        except KeyError:
            sys.exit(f"[ERROR] The state '{args.state}' was not found.")

    if args.county:
        try:
            get_world(date=args.date, county=args.county.capitalize()) # nopep8
        except KeyError:
                    sys.exit(f"[ERROR] The state '{args.state}' was not found.")

if __name__ == "__main__":
    main()
