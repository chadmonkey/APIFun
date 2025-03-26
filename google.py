from pytrends.request import TrendReq
import re

#pytrends = TrendReq(hl='en-US', tz=360, requests_args={'headers': {'User-Agent': 'Mozilla/5.0'}})
pytrends = TrendReq()

try:

    # Get today's trending searches
#    trending_searches = pytrends.trending_searches(pn='united_states')
    trending_searches = pytrends.trending_searches()
    print(trending_searches.head())

except Exception as e:
    print("Errpr:", e)
