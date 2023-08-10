import argparse
import json
import sys
import warnings
from datetime import datetime
from datetime import timedelta
from io import StringIO
from pathlib import Path

import pandas as pd
import requests
from colorama import Fore
from colorama import init
from requests.exceptions import HTTPError
from requests.exceptions import Timeout

__author__ = "DFIRSec (@pulsecode)"
__version__ = "0.0.3"
__description__ = "Retrieve Covid-19 stats by Country, State, and County"

TODAY = datetime.now().astimezone()
W_URL = (
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"
)
PARENT = Path(__file__).resolve().parent
DATA = PARENT.joinpath("data.json")

# Console Colors
init()
CYAN = Fore.CYAN
GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
RESET = Fore.RESET


def connect(url: str) -> requests.Response | None:
    """Connect to URL and return response."""
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/43.0"}
        resp = requests.get(url, timeout=5, headers=headers)
        if resp.status_code != 200:
            sys.exit(f"Failed to get data, Error Code: {resp.status_code}")
        else:
            return resp
    except HTTPError:
        print("HTTP Error:", HTTPError)
    except Timeout:
        print("Timeout encountered:", Timeout)
    except ConnectionError:
        print("Connection Error:", ConnectionError)
    return None


def get_world(date_sel: str = "", state: str = "", country: str = "", county: str = "") -> None:
    """Get Covid-19 data from URL and parse."""
    url = f"{W_URL}{TODAY.strftime('%m')}-{date_sel}-{TODAY.year}.csv"
    data = StringIO(connect(url).text)
    pd.set_option("display.max_rows", None)

    with pd.option_context("display.colheader_justify", "left"):
        columns = [1, 2, 3, 4, 7, 8, 9]
        data_frame = pd.read_csv(data, delimiter=",", usecols=columns, keep_default_na=False)

        def pct_confirmed(sel: str = "", opt: str = "") -> None:
            """Calculate percent of confirmed cases."""
            warnings.simplefilter("error", RuntimeWarning)
            confirmed = data_frame.loc[data_frame[sel] == opt]
            show_date = f"{YELLOW}Date: {TODAY.strftime('%m')}-{date_sel}-{TODAY.year}{RESET}"
            try:
                pct = (100.0 * confirmed["Deaths"].sum() / confirmed["Confirmed"].sum()).round(2).astype(str) + "%"
            except (UnboundLocalError, RuntimeWarning):
                print(
                    f"{Fore.RED}[Error]{Fore.RESET} Option argument, e.g., 'c' for County, 'w' for World, 's' for State"
                )
            else:
                print(f"{CYAN}{sel}: {opt}{RESET}\n{show_date}\n{('-' * 25)}")
                print(f"{'Total Confirmed:':16} {confirmed['Confirmed'].sum():,}")
                print(f"{'Total Deaths:':16} {confirmed['Deaths'].sum():,}")
                print(f"{'Death %:':16} {pct}")

        if "Deaths" in data_frame:
            if country:
                data_frame = data_frame.rename(
                    columns={"Admin2": "", "Province_State": "Province", "Country_Region": "Country"}
                )
                pct_confirmed(sel="Country", opt=country)

            if state:
                data_frame = data_frame.rename(
                    columns={"Admin2": "County", "Province_State": "State", "Country_Region": "Country"}
                )
                print(data_frame.loc[data_frame["State"] == state].to_string(index=False))
                pct_confirmed(sel="State", opt=state)

            if county:
                data_frame = data_frame.rename(
                    columns={"Admin2": "County", "Province_State": "State", "Country_Region": "Country"}
                )
                pct_confirmed(sel="County", opt=county)


def main() -> None:
    """Main function."""
    with open(DATA, encoding="utf-8") as json_file:
        json_data = json.load(json_file)

    d_date = datetime.now().astimezone() - timedelta(days=1)

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-w", "--country", help="Use 2 letter Country")
    group.add_argument("-s", "--state", help="Use 2 letter State")
    parser.add_argument("-c", "--county", help="Use 2 letter County")
    parser.add_argument("-d", "--date", default=d_date.strftime("%d"), help="Use 2 digit day, default is minus 1 day")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    if len(args.date) < 2:
        args.date = "0" + args.date

    if args.date >= TODAY.strftime("%d"):
        sys.exit(f"{RED}[ERROR]{RESET} Please use a date before: {datetime.now().astimezone.strftime('%m/%d/%Y')}")

    if args.country:
        try:
            get_world(date_sel=args.date, country=json_data["countries"][args.country.upper()])
        except KeyError:
            sys.exit(f"{RED}[ERROR]{RESET} The country '{args.country}' was not found.")

    if args.state:
        try:
            get_world(date_sel=args.date, state=json_data["states"][args.state.upper()])
        except KeyError:
            sys.exit(f"{RED}[ERROR]{RESET} The state '{args.state}' was not found.")

    if args.county:
        try:
            get_world(date_sel=args.date, county=args.county.title())
        except KeyError:
            sys.exit(f"{RED}[ERROR]{RESET} The county '{args.county}' was not found.")


if __name__ == "__main__":
    BANNER = r"""
       ______           _     __   ______                __
      / ____/___ _   __(_)___/ /  /_  __/________ ______/ /_____  _____
     / /   / __ \ | / / / __  /    / / / ___/ __ `/ ___/ //_/ _ \/ ___/
    / /___/ /_/ / |/ / / /_/ /    / / / /  / /_/ / /__/ ,< /  __/ /
    \____/\____/|___/_/\__,_/    /_/ /_/   \__,_/\___/_/|_|\___/_/

    """

    print(f"{CYAN}{BANNER}{RESET}")
    main()
