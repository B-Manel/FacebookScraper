import unittest
from scraper import Scraper


class TestScraper(unittest.TestCase):

    def test_posts(self):
        data = Scraper.data_scraper(page_name='nintendo')
        assert data is not None

