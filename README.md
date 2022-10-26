# PyTeslaStockScrape
##**A script that allows you to send notifications to any device once the tesla stock goes either below or above the inputted values.**
____________________________________________________________________________

This script uses ntfy.sh, a notification sending service by binwiederhier! [NTFY github](https://github.com/binwiederhier/ntfy)

Written in python, this script scrapes CNBC.com in order to gather TSLA and their stock market price.
____________________________________________________________________________
## **Features–**
- Send notifications once TSLA stock goes above or below the given value (Useful for selling or buying)
- Input the number of hours for the scraper to go
- Uses [ntfy.sh](https://ntfy.sh) for fast notifications across all your devices (Android, iOS, Windows, Linux, Mac, any platform!)
- Source code has lots of comments to guide you in figuring out how it works.
____________________________________________________________________________
## **Why?**
- I wanted to showcase how one can easily scrape data off a website and create an automated system to retrieve that specific piece of data.
____________________________________________________________________________
## **How?**
- I did so by using a regex which found the data between two keywords in the source code of the website. Note that the keywords vary between each website as the source code is different.
- I used urllib to get the source code of the URL and refresh that code every few seconds.
____________________________________________________________________________
## **User notice**
- Please note that you have to put your ntfy.sh channel in the code in order to receive the notifications!
- More info at ntfy.sh.
____________________________________________________________________________
## **Services used (Credits):**
- **ntfy.sh** by binwiederhier! Github Link: [NTFY](https://github.com/binwiederhier/ntfy)
- **urllib**, python library. Docs at [here](https://docs.python.org/3/library/urllib.html)
____________________________________________________________________________
## **Thank you.**
This was a fun little project demonstrating the power of python and integrating it into a notification service. Many more of these projects will come soon!

