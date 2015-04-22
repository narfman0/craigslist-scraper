craigslist-scraper
==================

Provide information for craigslist related metadata

Usage
-----

This is a developer focused library to provide information from craigslist.

    >>> from craigslist_scraper import scrape_url
    >>> data = scrape_url('http://craigslist.com/mcy/1234.html')
    >>> print(data.title)
    '2015 Victory Vegas 8-Ball'

License
-------

Copyright (c) 2015 Jon Robison

See included LICENSE for licensing information
