from django.test import TestCase
import services
import unittest
# Create your tests here.
#you need to decomment settings.configure() in services.py

class TestWikiStats(unittest.TestCase):
    def test_empty_input(self):
        res = services.findSummaryFromTitle("")  # False
        self.assertEqual(res, False)
    def test_unfound_article(self):
        res = services.findSummaryFromTitle("articlethatdoesnexist")  # False
        self.assertEqual(res, "")
    def test_return_summary(self):
        res = services.findSummaryFromTitle("Cambonilla")
        self.assertEqual(res, "Cambonilla is a genus of Cambodian and Laotian ant spiders first described by Rudy Jocqué in 2019. As of April 2019 it contains only two species.")
    def test_countFiveLetterWords(self):
        fk = services.findSummaryFromTitle("framework")
        res = services. countFiveLetterWords(fk)
        self.assertEqual(res, "More than 20% of words are 5+ letter words for that article's summary (13% > 4.8%).")
    def test_sendmail(self):
        se = services.sendMail()
        self.assertEqual(se, 1)

#OTHER TESTS HAVE BEEN COMPLETED, SUCH AS SENDING EMAIL FROM PYTHON CONSOLE
if __name__ == '__main__':
    unittest.main()