from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import services
from django.contrib import messages

@api_view()
def index(request):
    return Response({"message": "Welcome to Wiki stats app"})

#INSTRUCTION : create function based view in wiki_stats/views
# to return results of service in previous steps
@api_view()
def wikiStats(request, title=None):
    if title is not None:
        summary = services.findSummaryFromTitle(title)
        ct = services.countFiveLetterWords(summary)
        return Response({"message": ct})
    return Response({"message": "No result for that title"})

