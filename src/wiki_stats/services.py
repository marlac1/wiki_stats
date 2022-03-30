import wikipediaapi
import re
from django.core.mail import send_mail
from django.conf import settings
#from django.contrib import messages
#settings.configure()


#INSTRUCTION :  function to fetch summary section of a wikipedia page by passing title argument and using wikipedia api.
#input is title article chosen by the user from wikipedia en
#returns the article's summary
def findSummaryFromTitle(title):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    if len(title) > 0:
        article = wiki_wiki.page(title)
        #test page existence
        if article:
            return article.summary
        return False
    return False

#INSTRUCTIONS : alert + mail if more than 20% of words are 5+ letter words.
#input : return of findSummaryFromTitle(title)
#returns string alerts
def countFiveLetterWords(page_summary):
    ct = 0
    #transform str summary to a list of words without any punctuation
    if not page_summary:
        return "Article not found"
    page_summary_list = re.sub(r'[^\w\s]', '', page_summary).split(" ")

    for i in page_summary_list:
        if len(i) >= 5:
            ct += 1

    #compare nb of occurrences and 20% of the summary
    pct_summary = len(page_summary_list) * 2 / 10
    if ct > pct_summary:
        try:
            sendMail()
            return f"More than 20% of words are 5+ letter words for that article's summary ({ct}% > {pct_summary}%). An email has been sent."
        except:
            return f"More than 20% of words are 5+ letter words for that article's summary ({ct}% > {pct_summary}%)."
    return f"Less than 20% of words are 5+ letter words for that article's summary ({ct}% > {pct_summary}%)"

#dedicated sending mail function
def sendMail():
    return send_mail(
        subject='More than 20% of words are 5+ letter words',
        message='More than 20% of words are 5+ letter words',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.RECIPIENT_ADDRESS])

