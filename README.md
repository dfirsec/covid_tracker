Usage
```
usage: covid_tracker.py [-h] [-a] [-s STATE] [-c COUNTRY] [-d DATE]

optional arguments:
  -h, --help            show this help message and exit
  -a, --all             Results for all States
  -s STATE, --state STATE
                        Use 2 letter State
  -c COUNTRY, --country COUNTRY
                        Use 2 letter Country
  -d DATE, --date DATE  Use 2 digit day, default is minus 1 day
```


Report for all States
```
python covid_tracker.py -a
AK  Positive: 293      Deaths: 9      3.07%
AL  Positive: 4,113    Deaths: 121    2.94%
AR  Positive: 1,569    Deaths: 33     2.1%
AS  Positive: 0        Deaths: 0
AZ  Positive: 3,962    Deaths: 142    3.58%
CA  Positive: 24,424   Deaths: 821    3.36%
CO  Positive: 7,941    Deaths: 329    4.14%
CT  Positive: 14,755   Deaths: 868    5.88%
DC  Positive: 2,197    Deaths: 72     3.28%
DE  Positive: 2,014    Deaths: 46     2.28%
FL  Positive: 22,511   Deaths: 609    2.71%
GA  Positive: 14,987   Deaths: 552    3.68%
GU  Positive: 135      Deaths: 5      3.7%
HI  Positive: 517      Deaths: 9      1.74%
IA  Positive: 1,995    Deaths: 53     2.66%
ID  Positive: 1,464    Deaths: 39     2.66%
IL  Positive: 24,593   Deaths: 948    3.85%
IN  Positive: 8,955    Deaths: 436    4.87%
KS  Positive: 1,494    Deaths: 76     5.09%
KY  Positive: 2,210    Deaths: 115    5.2%
LA  Positive: 21,951   Deaths: 1,103  5.02%
MA  Positive: 29,918   Deaths: 1,108  3.7%
MD  Positive: 10,032   Deaths: 349    3.48%
ME  Positive: 770      Deaths: 24     3.12%
MI  Positive: 28,059   Deaths: 1,921  6.85%
MN  Positive: 1,809    Deaths: 87     4.81%
MO  Positive: 4,895    Deaths: 147    3.0%
MP  Positive: 13       Deaths: 2      15.38%
MS  Positive: 3,360    Deaths: 122    3.63%
MT  Positive: 404      Deaths: 7      1.73%
NC  Positive: 5,123    Deaths: 117    2.28%
ND  Positive: 365      Deaths: 9      2.47%
NE  Positive: 901      Deaths: 20     2.22%
NH  Positive: 1,139    Deaths: 32     2.81%
NJ  Positive: 71,030   Deaths: 3,156  4.44%
NM  Positive: 1,407    Deaths: 36     2.56%
NV  Positive: 3,211    Deaths: 131    4.08%
NY  Positive: 213,779  Deaths: 11,586 5.42%
OH  Positive: 7,791    Deaths: 361    4.63%
OK  Positive: 2,263    Deaths: 123    5.44%
OR  Positive: 1,663    Deaths: 58     3.49%
PA  Positive: 26,490   Deaths: 647    2.44%
PR  Positive: 974      Deaths: 51     5.24%
RI  Positive: 3,529    Deaths: 87     2.47%
SC  Positive: 3,656    Deaths: 107    2.93%
SD  Positive: 1,168    Deaths: 6      0.51%
TN  Positive: 6,079    Deaths: 135    2.22%
TX  Positive: 15,492   Deaths: 364    2.35%
UT  Positive: 2,542    Deaths: 20     0.79%
VA  Positive: 6,500    Deaths: 195    3.0%
VI  Positive: 51       Deaths: 1      1.96%
VT  Positive: 759      Deaths: 30     3.95%
WA  Positive: 10,694   Deaths: 541    5.06%
WI  Positive: 3,721    Deaths: 182    4.89%
WV  Positive: 702      Deaths: 10     1.42%
WY  Positive: 287      Deaths: 2      0.7%

Total: 632,656 | Deaths: 28,160 (4.45%)
```


Individual State report
```
python covid_tracker.py -s ny
             Admin2 Province_State Country_Region          Last_Update  Confirmed  Deaths  Recovered Percentage
24           Albany       New York             US  2020-04-15 22:56:51        548      20          0      3.65%
35         Allegany       New York             US  2020-04-15 22:56:51         28       1          0      3.57%
242          Broome       New York             US  2020-04-15 22:56:51        153       8          0      5.23%
377     Cattaraugus       New York             US  2020-04-15 22:56:51         32       0          0       0.0%
378          Cayuga       New York             US  2020-04-15 22:56:51         36       1          0      2.78%
405      Chautauqua       New York             US  2020-04-15 22:56:51         24       3          0      12.5%
410         Chemung       New York             US  2020-04-15 22:56:51         69       1          0      1.45%
411        Chenango       New York             US  2020-04-15 22:56:51         71       0          0       0.0%
503         Clinton       New York             US  2020-04-15 22:56:51         45       3          0      6.67%
531        Columbia       New York             US  2020-04-15 22:56:51        100      10          0      10.0%
557        Cortland       New York             US  2020-04-15 22:56:51         23       0          0       0.0%
663        Delaware       New York             US  2020-04-15 22:56:51         46       3          0      6.52%
722        Dutchess       New York             US  2020-04-15 22:56:51       2048      18          0      0.88%
761            Erie       New York             US  2020-04-15 22:56:51       1812     101          0      5.57%
768           Essex       New York             US  2020-04-15 22:56:51         12       0          0       0.0%
841        Franklin       New York             US  2020-04-15 22:56:51         13       0          0       0.0%
864          Fulton       New York             US  2020-04-15 22:56:51         24       0          0       0.0%
890         Genesee       New York             US  2020-04-15 22:56:51         76       2          0      2.63%
963          Greene       New York             US  2020-04-15 22:56:51         73       0          0       0.0%
1002       Hamilton       New York             US  2020-04-15 22:56:51          3       0          0       0.0%
1075       Herkimer       New York             US  2020-04-15 22:56:51         40       3          0       7.5%
1209      Jefferson       New York             US  2020-04-15 22:56:51         47       0          0       0.0%
1405          Lewis       New York             US  2020-04-15 22:56:51          7       0          0       0.0%
1452     Livingston       New York             US  2020-04-15 22:56:51         34       3          0      8.82%
1515        Madison       New York             US  2020-04-15 22:56:51        110       3          0      2.73%
1689         Monroe       New York             US  2020-04-15 22:56:51        884      56          0      6.33%
1709     Montgomery       New York             US  2020-04-15 22:56:51         32       1          0      3.12%
1758         Nassau       New York             US  2020-04-15 22:56:51      26715    1057          0      3.96%
1776  New York City       New York             US  2020-04-15 22:56:51     118302    8455          0      7.15%
1788        Niagara       New York             US  2020-04-15 22:56:51        229       9          0      3.93%
1839         Oneida       New York             US  2020-04-15 22:56:51        246       4          0      1.63%
1841       Onondaga       New York             US  2020-04-15 22:56:51        563      12          0      2.13%
1843        Ontario       New York             US  2020-04-15 22:56:51         62       0          0       0.0%
1848         Orange       New York             US  2020-04-15 22:56:51       5830     178          0      3.05%
1856        Orleans       New York             US  2020-04-15 22:56:51         33       0          0       0.0%
1866         Oswego       New York             US  2020-04-15 22:56:51         42       2          0      4.76%
1871         Otsego       New York             US  2020-04-15 22:56:51         44       3          0      6.82%
2042         Putnam       New York             US  2020-04-15 22:56:51        634       7          0       1.1%
2077     Rensselaer       New York             US  2020-04-15 22:56:51        140       6          0      4.29%
2118       Rockland       New York             US  2020-04-15 22:56:51       8474     298          0      3.52%
2182       Saratoga       New York             US  2020-04-15 22:56:51        227       4          0      1.76%
2188    Schenectady       New York             US  2020-04-15 22:56:51        237       8          0      3.38%
2190      Schoharie       New York             US  2020-04-15 22:56:51         20       0          0       0.0%
2193       Schuyler       New York             US  2020-04-15 22:56:51          8       0          0       0.0%
2217         Seneca       New York             US  2020-04-15 22:56:51         18       0          0       0.0%
2295   St. Lawrence       New York             US  2020-04-15 22:56:51         92       0          0       0.0%
2324        Steuben       New York             US  2020-04-15 22:56:51        151      16          0      10.6%
2340        Suffolk       New York             US  2020-04-15 22:56:51      23523     653          0      2.78%
2344       Sullivan       New York             US  2020-04-15 22:56:51        424      10          0      2.36%
2407          Tioga       New York             US  2020-04-15 22:56:51         25       0          0       0.0%
2420       Tompkins       New York             US  2020-04-15 22:56:51        118       0          0       0.0%
2454         Ulster       New York             US  2020-04-15 22:56:51        745      13          0      1.74%
2485     Unassigned       New York             US  2020-04-15 22:56:51          0       0          0       nan%
2579         Warren       New York             US  2020-04-15 22:56:51         77       0          0       0.0%
2607     Washington       New York             US  2020-04-15 22:56:51         42       2          0      4.76%
2633          Wayne       New York             US  2020-04-15 22:56:51         48       0          0       0.0%
2655    Westchester       New York             US  2020-04-15 22:56:51      20947     640          0      3.06%
2731        Wyoming       New York             US  2020-04-15 22:56:51         42       3          0      7.14%
2740          Yates       New York             US  2020-04-15 22:56:51          6       0          0       0.0%
```


Country Report
```
python covid_tracker.py -c cn
     Admin2  Province_State Country_Region          Last_Update  Confirmed  Deaths  Recovered Percentage
2760                  Anhui          China  2020-04-09 01:12:20        991       6        984      0.61%
2763                Beijing          China  2020-04-15 01:12:53        590       8        495      1.36%
2770              Chongqing          China  2020-03-29 00:14:12        579       6        570      1.04%
2777                 Fujian          China  2020-04-15 01:53:31        353       1        331      0.28%
2778                  Gansu          China  2020-04-14 14:31:10        139       2        136      1.44%
2785              Guangdong          China  2020-04-15 01:45:25       1566       8       1462      0.51%
2786                Guangxi          China  2020-04-02 00:16:02        254       2        252      0.79%
2787                Guizhou          China  2020-03-18 01:37:43        146       2        144      1.37%
2788                 Hainan          China  2020-03-24 04:19:14        168       6        162      3.57%
2789                  Hebei          China  2020-04-14 01:49:04        327       6        314      1.83%
2790           Heilongjiang          China  2020-04-15 00:40:21        841      13        470      1.55%
2791                  Henan          China  2020-04-14 00:43:57       1276      22       1254      1.72%
2792              Hong Kong          China  2020-04-15 14:46:10       1017       4        459      0.39%
2793                  Hubei          China  2020-04-15 01:45:25      67803    3222      64402      4.75%
2794                  Hunan          China  2020-04-02 01:30:57       1019       4       1014      0.39%
2795         Inner Mongolia          China  2020-04-15 00:31:14        190       1         94      0.53%
2797                Jiangsu          China  2020-04-15 01:12:53        653       0        642       0.0%
2798                Jiangxi          China  2020-04-10 01:22:42        937       1        936      0.11%
2799                  Jilin          China  2020-04-15 00:28:05        102       1         96      0.98%
2800               Liaoning          China  2020-04-14 00:18:37        145       2        138      1.38%
2801                  Macau          China  2020-04-15 14:46:10         45       0         16       0.0%
2810                Ningxia          China  2020-03-16 08:47:05         75       0         75       0.0%
2818                Qinghai          China  2020-02-23 11:19:02         18       0         18       0.0%
2827                Shaanxi          China  2020-04-15 01:20:59        256       3        251      1.17%
2828               Shandong          China  2020-04-15 00:52:31        784       7        761      0.89%
2829               Shanghai          China  2020-04-15 06:12:32        622       7        485      1.13%
2830                 Shanxi          China  2020-04-15 00:28:05        186       0        135       0.0%
2831                Sichuan          China  2020-04-15 01:04:46        560       3        550      0.54%
2836                Tianjin          China  2020-04-15 13:31:10        185       3        171      1.62%
2837                  Tibet          China  2020-02-23 11:19:02          1       0          1       0.0%
2842               Xinjiang          China  2020-03-08 05:31:02         76       3         73      3.95%
2844                 Yunnan          China  2020-04-15 00:18:56        184       2        176      1.09%
2845               Zhejiang          China  2020-04-15 02:05:41       1268       1       1244      0.08%
```
