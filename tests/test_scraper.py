import unittest
from craigslist_scraper.scraper import scrape_html

TEST_DATA = '<section class="body"><h2 class="postingtitle"><span class="star"></span>  2014 Victory Vegas 8 Ball - <span class="price">$7000</span><small> (Norfolk)</small>\
</h2><section class="userbody"><div class="mapAndAttrs"><p class="attrgroup"><span><b>2014 Victory Vegas 8 Ball</b></span> <span>odometer: <b>7</b></span> \
<span>paint color : <b>black</b></span> <span>fuel : <b>gas</b></span><span>transmission : <b>manual</b></span></p><p class="attrgroup"><span>condition: <b>like new</b></span>\
<br></p></div><section id="postingbody">Selling my whatever.</section></section>'


class TestScraper(unittest.TestCase):
    def test_scrape_html(self):
        data = scrape_html(TEST_DATA)
        self.assertEqual(data.price, 7000)
        self.assertEqual(data.title, '2014 Victory Vegas 8 Ball')
        self.assertEqual(data.attrs['paint color'], 'black')


if __name__ == '__main':
    unittest.main()
