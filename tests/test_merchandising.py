import unittest
from lxml import objectify

from ebay.merchandising import *

keywords = "ipod"
categoryId = "73839" #iPods & MP3 Players #


class TestMerchandisingApi(unittest.TestCase):
    def test_getDeals(self):
        result = getDeals(keywords=keywords, encoding="XML")
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Success")


    def test_getMostWatchedItems(self):
        result = getMostWatchedItems(affiliate=None, maxResults=None,categoryId=None, encoding="XML")
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Success")


    def test_getRelatedCategoryItems(self):
        result = getRelatedCategoryItems(affiliate=None,
                                       maxResults=None, \
                                       categoryId=categoryId, \
                                       itemFilter=None, \
                                       itemId=None, \
                                       encoding="XML")
#        print result
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Success")


    def test_getSimilarItems(self):
        result = getSimilarItems(affiliate=None, \
                      maxResults=None, \
                      categoryId=None, \
                      categoryIdExclude=[], \
                      endTimeFrom=None, \
                      endTimeTo=None, \
                      itemFilter=None, \
                      itemId=None, \
                      listingType=None, \
                      maxPrice=None, \
                      encoding="XML")
        print result
#        The problem is that the service is expecting an itemId, "string - The ID of an active item listing or a listing that has ended less than two weeks ago.Max length: 19."
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Success")


    def test_getTopSellingProducts(self):
        result = getTopSellingProducts(affiliate=None, maxResults=None, encoding="XML")
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Success")


if __name__ == '__main__':
    unittest.main()
