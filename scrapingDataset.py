from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

#Web scraping dataset for LOTR knowledge
data = ''
url = "https://en.wikipedia.org/wiki/The_Lord_of_the_Rings:_The_Fellowship_of_the_Ring#Plot"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

# erase script and style elements
for script in soup(["script","style"]):
    script.extract() #erase it

# get all text except references, in lower case and delete "[x]"
with open('./{}.txt'.format("lotr_story2"),mode='wt', encoding='utf-8') as file:
    for data in soup.find_all("p"):
        file.write(re.sub(r'[\(\[].*?[\)\]]', '', data.get_text().lower()))
