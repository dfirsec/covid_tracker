import argparse
import csv
import json
import re
import sys
from datetime import date, datetime, timedelta
from io import StringIO
from pathlib import Path
from pprint import pprint

import pandas as pd
import requests
from colorama import Back, Fore, Style, init
from requests.exceptions import (ConnectTimeout, HTTPError, RequestException,
                                 Timeout)

init()

today = date.today()
now = datetime.now()
BASE_URL = 'https://covidtracking.com/api'
BASE_DIR = Path(__file__).resolve().parent
DATA = BASE_DIR.joinpath('data.json')

with open(DATA) as json_file:
    json_data = json.load(json_file)


def connect(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/43.0"}  # nopep8
        resp = requests.get(url, timeout=5, headers=headers)
        if resp.status_code != 200:
            quit(f'Failed to get data, Error Code: {resp.status_code}')
        else:
            return resp
    except HTTPError:
        print("HTTP Error:", HTTPError)
    except Timeout:
        print("Timeout encountered:", Timeout)
    except ConnectionError:
        print("Connection Error:", ConnectionError)
    except RequestException:
        quit("Issue encountered:", RequestException)


def get_state_info(state=None):
    url = BASE_URL + f"/states/info?state={state}"
    if connect(url).json():
        info = connect(url).json()
        print(f"\nState Link:\n{info['covid19Site']:<6}\n")
        print(f"Notes:\n{info['notes']:<6}")


def get_all_states(date=None):
    url = BASE_URL + f"/states/daily?date={today.year}{today.strftime('%m')}{date}"  # nopep8
    if connect(url).json():
        sp = []  # state positives
        sd = []  # state deaths
        for s in connect(url).json():
            if 'death' in s and s['death'] != 0:
                sp.append(s['positive'])
                sd.append(s['death'])
                percent = s['death'] / s['positive'] * 100
                print(f"{s['state']:3} Positive: {s['positive']:<8,} Deaths: {s['death']:<6,} {round(percent, 2)}%")  # nopep8
            elif 'death' in s:
                percent = s['death'] / s['positive'] * 100
                if s['death'] == 0:
                    print(f"{Fore.GREEN}{s['state']:3} Positive: {s['positive']:<8,} Deaths: {s['death']:<6,} {round(percent, 2)}%{Style.RESET_ALL}")  # nopep8
                else:
                    print(f"{s['state']:3} Positive: {s['positive']:<8,} Deaths: {s['death']:<6,} {round(percent, 2)}%")  # nopep8
            else:
                print(f"{Fore.GREEN}{s['state']:3} Positive: {s['positive']:<8,} Deaths: 0{Style.RESET_ALL}")  # nopep8

        print(f"\n{Fore.RED}Total: {sum(sp):,} | Deaths: {sum(sd):,} ({round(sum(sd)/sum(sp)*100, 2)}%){Style.RESET_ALL}")  # nopep8


def get_worldwide(date=None, state=None, country=None):
    url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{today.strftime('%m')}-{date}-{today.year}.csv"
    data = StringIO(connect(url).text)
    pd.set_option('display.max_rows', None)
    columns = [1, 2, 3, 4, 7, 8, 9]
    df = pd.read_csv(data, delimiter=',', usecols=columns, keep_default_na=False)  # nopep8
    if 'Deaths' in df:
        df["Percentage"] = (100. * df['Deaths']/df['Confirmed']).round(2).astype(str) + '%'  # nopep8
        if country:
            print(f"{df.loc[df['Country_Region'] == country]}")
        if state:
            print(f"{df.loc[df['Province_State'] == state]}")


def main():
    d_date = datetime.today() - timedelta(days=1)

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-a', '--all', action='store_true',
                       help="Results for all States")
    parser.add_argument('-s', '--state',
                        help="Use 2 letter State")
    parser.add_argument('-c', '--country',
                        help="Use 2 letter Country")
    parser.add_argument('-d', '--date', default=d_date.strftime("%d"),
                        help="Use 2 digit day, default is minus 1 day")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        quit(1)

    if args.all:
        get_all_states(date=args.date)

    if args.country:
        try:
            get_worldwide(date=args.date, country=json_data['countries'][args.country.upper()])  # nopep8
        except KeyError:
            quit(f"[ERROR] The country '{args.country}' was not found.")

    if args.state:
        try:
            get_worldwide(date=args.date,
                          state=json_data['states'][args.state.upper()])
        except KeyError:
            quit(f"[ERROR] The state '{args.state}' was not found.")


if __name__ == "__main__":
    main()
