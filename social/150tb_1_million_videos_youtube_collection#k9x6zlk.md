I do a similar thing. I generally download bestaudio but only up to 480p video. I wrote my own software to manage it and check ~10,000+ channels (at hourly intervals between once per day and once per year depending on how frequently new videos are available).


    $ library history downloaded /home/xk/lb/video.db 
    Downloaded media:
    month    total_duration                           avg_duration                total_size    avg_size    count
    -------  ---------------------------------------  ------------------------  ------------  ----------  -------
    2023-06  5 years, 10 months, 26 days and 5 hours  17 minutes                     13.0 TB     71.7 MB   181620
    2023-07  19 days and 23 hours                     50 minutes                    310.5 GB    537.3 MB      578
    2023-08  25 days and 17 hours                     22 minutes                    123.4 GB     73.3 MB     1682
    2023-09  23 years, 10 months, 3 days and 6 hours  22 minutes                     52.9 TB     92.4 MB   572712
    2023-10  8 months, 20 days and 18 hours           27 minutes                      1.4 TB     96.8 MB    14151
    2023-11  3 months, 0 days and 13 hours            31 minutes                    437.7 GB    102.5 MB     4272

I have a lot more audio only:

    $ library history downloaded /home/xk/lb/audio.db 
    Downloaded media:
    month    total_duration                           avg_duration                total_size    avg_size    count
    -------  ---------------------------------------  ------------------------  ------------  ----------  -------
    2023-06  26 years, 4 months, 12 days and 6 hours  13 minutes                      5.4 TB      5.3 MB  1029088
    2023-07  4 days and 59 minutes                    8 minutes and 20 seconds        3.3 GB      4.8 MB      698
    2023-08  4 days and 15 hours                      11 minutes                      3.6 GB      5.9 MB      605
    2023-09  39 years, 9 months, 2 days and 10 hours  8 minutes and 49 seconds       15.7 TB      6.6 MB  2367739
    2023-10  2 years, 1 month, 4 days and 8 hours     7 minutes and 54 seconds        1.0 TB      7.4 MB   139315
    2023-11  42 years, 2 months, 1 day and 3 hours    1 hour and 18 minutes           5.3 TB     18.6 MB   283524

https://github.com/chapmanjacobd/library
