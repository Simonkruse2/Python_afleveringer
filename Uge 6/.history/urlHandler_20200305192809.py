from .NotFoundException import NotFoundException
import pandas as pd
import requests

class urlHandler():
    def __init__(self, url_list):
        self.url_list =[]
        for url in url_list:
            self.url_list.append(url)
    
    def download(self, url):
        if requests.head(url) == 404:
            raise NotFoundException()
        else:
            re = requests.get(url)
    
    def multidownload(self, url_list):
        # uses threads to download multiple urls as text and stores filenames as a property
        pass

    def iter(self):
        # returns an iterator
        pass

    def next(self):
        # returns the next filename (and stops when there are no more)
        pass

    def urllist_generator(self):
        # returns a generator to loop through the urls
        pass

    def avg_vowels(self, text):
        # a rough estimate on readability returns average number of vowels in the words of the text
        pass

    def hardest_read(self):
        # returns the filename of the text with the highest vowel score (use all the cpu cores on the computer for this work.
        pass
urlHandler.download('https://www.gutenberg.org/files/1342/1342-0.txt')
# download('https://www.gutenberg.org/files/1342/1342-0.txt')