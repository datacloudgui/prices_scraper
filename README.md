# Price scraper for a colombian technology vendor

Python scraper using beautifulsoup

## Requered packages

```python
import yaml
import requests
import bs4
import urllib.request
import argparse
import logging
import csv
import datetime
```

## Usage

Four files are disposed:

- **config.yaml:** You can put the URL to be scrapped. The file allow organize by retail site, category and queries.

- **common.py:** A simple python code to import and parse the previous .yaml file.

- **item_page_object.py:** Python class to read the page and provide a method to extract all articles of that page.

  The constructor requires: the base URL (without page number), the category of products to be extracted and the total number of pages.

- **prices-scraper.py:** The principal code with 3 arguments:

  1. Retail site to be scraped (only alkosto are used at the moment).
  2. Category of the product - twelve categories implemented at the moment.
  3. Number of pages to scrap in the selected categories

  ##example: 
  
  python3 prices_scraper.py alkosto televisores 3
  python3 prices_scraper.py alkosto computadores-tablets 6

  The code use the Homepage class into a for loop to collect all the data of the selected category and saving on a csv file.

  Some logging messages are used to inform the user about the progress telling at the end the total of articles founded.

Finally, an example of the exported data is provided

## Next Steps

Improve the use of config.yaml to be the unique file to be changed if the sraped page change.

The cleaning and reporting code will be available soon.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
