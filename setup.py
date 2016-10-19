from setuptools import setup, find_packages
from craigslist_scraper import __version__ as version


setup(
    name='craigslist-scraper',
    version=version,
    description=('Provide information for craigslist related metadata'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='craigslist scraper meta',
    author='Jon Robison',
    author_email='narfman0@gmail.com',
    url='https://github.com/narfman0/craigslist-scraper',
    license='LICENSE',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['craigslist_scraper.scraper'],
    zip_safe=True,
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    test_suite='tests',
)
