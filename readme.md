# Read this carefully

### Description
The following program will run through the prothom-alo archive and scrape the titles out of the pages and save it in a text file. 

The crawler.py file uses the scraper.py file as a module and generates urls for the module to scrape data from. Entire code is very straight forward. Let me know if you have any query.

### How to use
You can run the program in two ways. 

1. Run from terminal with dates as parameters. 

> `python crawler.py <from_date> <to_date>`

In this method you can directly give the dates as parameters.

**from_date**

A date to start scrape from in following format _dd.mm.yyyy_ (i.e. 10.01.2019)

**to_date**

A date to stop scrape at in following format _dd.mm.yyyy_ (i.e. 10.01.2019)

So a complete command looks like 
> `python crawler.py 08.01.2019 09.01.2019`

2. Or you can simply run 
> `python crawler.py` 

to input the dates in on screen queries.

After the crawling and scraping is finished all the titles are stored in a text files named <date>.txt in the output folder. They are all produced individually for the dates.

Then run 
> `python merge.py` 

This will merge all the news files into one single file out.txt 