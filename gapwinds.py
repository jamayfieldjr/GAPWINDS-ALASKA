#import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import re

quote_page = "https://www.aviationweather.gov/metar/data?ids=++PACV+PANC+PAMR++PAED++&format=raw&date=&hours=0"


html = urlopen(quote_page)
soup = BeautifulSoup(html,"html.parser")
#features = "html.parser"
text = str(soup.find_all('code'))

def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

#print(remove_html_tags(text))
cleantext=remove_html_tags(text) 
cleantext=re.split(",",cleantext)

for values in cleantext:
  print(values);

print(' ')

