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
County         State     Country Last_Update           Confirmed  Deaths  Recovered Percentage
        Albany  New York  US      2020-05-05 02:32:34    1287        49   0           3.81%
      Allegany  New York  US      2020-05-05 02:32:34      35         0   0            0.0%
        Broome  New York  US      2020-05-05 02:32:34     334        22   0           6.59%
   Cattaraugus  New York  US      2020-05-05 02:32:34      53         0   0            0.0%
        Cayuga  New York  US      2020-05-05 02:32:34      51         1   0           1.96%
    Chautauqua  New York  US      2020-05-05 02:32:34      37         4   0          10.81%
       Chemung  New York  US      2020-05-05 02:32:34     126         1   0           0.79%
...
-------------------------
Total Confirmed: 318,953
Total Deaths:    24,999
```

County report
```
python covid_tracker.py -c Albany
County  State     Country Last_Update           Confirmed  Deaths  Recovered Percentage
 Albany  New York  US      2020-05-05 02:32:34  1287       49      0          3.81% 
```


Country Report
```
python covid_tracker.py -c cn
China
-------------------------
Total Confirmed:  83,966
Total Deaths:     4,637
```
