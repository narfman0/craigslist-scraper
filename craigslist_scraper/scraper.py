""" Library entry point """
import re, requests
from bs4 import BeautifulSoup

class CLScrape(object):
    """ Scraper object to hold data """
    def __init__(self, soup):
        """ Initialize and scrape """
        self.soup = soup
        self.title = self.parse_title()
        try:
            self.price = self.parse_int('.price')
        except:
            self.price = 'Unlisted'
        self.attrs = {}
        for attrgroup in soup.select('.attrgroup'):
            for attr in attrgroup('span'):
                if attr.b and attr.text != attr.b.text:
                    self.parse_attr(attr)
        for attr in soup.select('.bigattr'):
            self.parse_attr(attr)

    def parse_attr(self, attr):
        """ Parse a single attribute from the BeautifulSoup tag """
        name = self.get_text(attr).strip(' :')
        value = attr.b.text.strip()
        self.attrs[name] = value

    def parse_title(self):
        """ Extract title from a listing. CL does it inconsistently, thus takes
        some extra effort """
        try:
            return self.parse_string('.postingtitletext').strip(' -')
        except:
            # looks like CL are transitioning to this selector? wasn't here
            # yesterday
            pass
        #fallback mechanism(s)
        return self.soup.find(class_='postingtitle').text.strip()

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
    return CLScrape(BeautifulSoup(html, "html.parser"))


def scrape_url(url):
    """ Scrape a given url for information """
    html = requests.get(url).text
    return scrape_html(html)
