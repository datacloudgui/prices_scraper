import argparse
import logging
import csv
import datetime
logging.basicConfig(level=logging.INFO)

import item_page_objects as pages
from common import config


logger = logging.getLogger(__name__)


def _prices_scraper(retail_site, category_id, num_pages):

    page = config()['retail_sites'][retail_site][category_id]

    logging.info('Beginning scraper for {}'.format(page))
    logging.info('Finding articles...')
    all_articles_title=[]
    all_articles_price=[]
    all_articles_link=[]
    all_articles_image=[]
    for i in range(1,num_pages+1):
        articles_title, articles_price, link_list, image_list = _find_article_info_in_page(retail_site,category_id,str(i))
        all_articles_title+=articles_title
        all_articles_price+=articles_price
        all_articles_link+=link_list
        all_articles_image+=image_list
    
    logging.info('{num_articles} articles info found in {num_pages} pages'.format(num_articles=len(all_articles_title), num_pages=num_pages))
    _save_articles_to_csv(category_id,all_articles_title,all_articles_price,all_articles_link,all_articles_image)

def _save_articles_to_csv(category_id,articles_title, articles_price,articles_link, articles_image):
    now = datetime.datetime.now()
    csv_headers = 'categoria','producto',now.strftime('%d_%m_')+now.strftime("%y"),'link','imagen'
    out_file_name = '{category_id}_{datetime}.csv'.format(category_id=category_id, datetime=now.strftime('%d_%m_')+now.strftime("%y"))

    with open(out_file_name, mode='w+') as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)

        for i in range(0,len(articles_title)):
            row = [category_id,articles_title[i],articles_price[i].strip(),articles_link[i],articles_image[i]]
            writer.writerow(row)

def _find_article_info_in_page(news_site_uid,category_id,page):
    page = pages.HomePage(news_site_uid,category_id,page)

    return page.articles

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    retail_site_choices = list(config()['retail_sites'].keys())
    parser.add_argument('retail_site',
                        help='The retail site that you want to scrape',
                        type=str,
                        choices=retail_site_choices)

    parser.add_argument('category_id',
                        help='The category of articles that you want to scrape',
                        type=str)

    parser.add_argument('num_pages',
                        help='The number of pages in the selected category',
                        type=int)

    args = parser.parse_args()
    _prices_scraper(args.retail_site, args.category_id, args.num_pages)

