""" Library entry point """
import re, requests
from bs4 import BeautifulSoup

class CLScrape(object):
    """ Scraper object to hold data """
    def __init__(self, soup):
        """ Initialize and scrape """
        self.soup = soup
        # title is not consistent to fetch
        title_tag = soup.find(class_='postingtitle')
        self.title = title_tag.text
        if '-' in self.title and (title_tag.small or '$' in self.title):
            self.title = self.title.split('-')[0].strip()

        self.price = self.parse_int('.price')
        self.attrs = {}
        for attrgroup in soup.select('.attrgroup'):
            for attr in attrgroup('span'):
                if attr.b and attr.text != attr.b.text:
                    attribute_name = self.get_text(attr).strip(' :')
                    attribute_value = attr.b.text.strip()
                    self.attrs[attribute_name] = attribute_value

    def parse_string(self, selector):
        """ Parse first string matching selector """
        return self.get_text(self.soup.select(selector)[0])

    def parse_int(self, selector):
        """ Extract one integer element from soup """
        return int(re.sub('[^0-9]', '', self.parse_string(selector)))

    def get_text(self, item):
        """ Non-recursively extract text from an item """
        return item.find(text=True, recursive=False).strip()


def scrape_html(html):
    """ Return meta information about a video """
    return CLScrape(BeautifulSoup(html))


def scrape_url(url):
    """ Scrape a given url for information """
    html = requests.get(url).text
    return scrape_html(html)
