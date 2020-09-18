Usage
```
usage: covid_tracker.py [-h] [-w COUNTRY | -s STATE | -c COUNTY] [-d DATE]

optional arguments:
  -h, --help            show this help message and exit
  -w COUNTRY, --country COUNTRY
                        Use 2 letter Country
  -s STATE, --state STATE
                        Use 2 letter State
  -c COUNTY, --county COUNTY
                        Use 2 letter County
  -d DATE, --date DATE  Use 2 digit day, default is minus 1 day
```


Individual State report
```
python covid_tracker.py -s ny
County         State     Country Last_Update           Confirmed  Deaths  Recovered
        Albany  New York  US      2020-05-11 02:32:30    1432        59   0
      Allegany  New York  US      2020-05-11 02:32:30      36         0   0
        Broome  New York  US      2020-05-11 02:32:30     373        23   0
   Cattaraugus  New York  US      2020-05-11 02:32:30      60         0   0
        Cayuga  New York  US      2020-05-11 02:32:30      58         1   0
...
State: New York
-------------------------
Total Confirmed: 335,395
Total Deaths:    26,641
Percentage:      7.94%
```

County report
```
python covid_tracker.py -c Albany
County: Albany
-------------------------
Total Confirmed: 1,440
Total Deaths:    59
Percentage:      4.1%
```


Country Report
```
python covid_tracker.py -w cn
Country: China
-------------------------
Total Confirmed: 84,010
Total Deaths:    4,637
Percentage:      5.52%
```
