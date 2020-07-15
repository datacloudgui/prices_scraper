import requests
import bs4
import urllib.request
import datetime
from common import config


class HomePage:

    def __init__(self, price_site_uid, category_id,num_page):
        self._config = config()['retail_sites'][price_site_uid]
        self._queries = self._config['queries']
        self._html = None
        #Visit the selected page creating the correct URL during calling
        self._visit(self._config[category_id]+'?p='+num_page,category_id,num_page)

    @property
    def articles(self):
        title_list = []
        price_list = []
        link_list = []
        image_list = []
        for article in self._select(self._queries['articulo']):
            try:
                #The main articles to obtain must have this tag
                link_list.append(article.h2.a['href'])
            except:
                #Avoiding articles without link tag
                print('Dont have link, skipped')
                continue
            try:
                #HTML tags for product name, price and image source
                title_list.append(article.a['title'])
                price_list.append(article.find("span","price").span.string)
                image_list.append(article.find("img", "lazy")['data-src'])
            except:
                print('Dont have any of the requered tags')
        
        print('Length of title: '+str(len(title_list)))
        print('Price: '+str(len(price_list)) + 'Last value: '+ str(price_list[len(price_list)-1]) )
        print('Link: '+str(len(link_list)) + 'Last value: '+ str(link_list[len(link_list)-1]) )
        print('Images: '+str(len(image_list)) + 'Last value: '+ str(image_list[len(image_list)-1]) )
        return title_list, price_list, link_list, image_list

    def _select(self, query_string):
        nodes = self._html.select(query_string)

        if not nodes:
            return None

        return nodes

    def _visit(self, url,category_id,num_page):
        now = datetime.datetime.now()
        response = requests.get(url)

        response.raise_for_status()
        
        #copy of page to store the original HTML text
        response2 = urllib.request.urlopen(url)
        webContent = response2.read()
        f = open('fuente'+'/'+category_id+'/'+num_page+now.strftime('%d_%m_')+now.strftime("%y")+'.html', 'wb')
        f.write(webContent)
        f.close

        self._html = bs4.BeautifulSoup(response.text, 'html.parser')

