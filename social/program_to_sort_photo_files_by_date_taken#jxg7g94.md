because you said file explorer I assume you are on Windows

https://exiftool.org/exiftool-12.65.zip

> The next step I want to take is sorting her files in folders by [Year > Month]

https://exiftool.org/#filename

> If you want to move files automatically to YEAR / MONTH / original_filename:
>  a new directory can be specified by setting the value of the Directory tag. For example, the following command moves all images originally in directory "DIR" into a directory hierarchy organized by year/month/day:

    exiftool "-Directory<DateTimeOriginal" -d "%Y/%m/%d" DIR
