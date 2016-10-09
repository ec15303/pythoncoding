import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import random
from collections import Counter
from nltk.corpus import stopwords
import urllib2
from bs4 import BeautifulSoup
import re

url = raw_input('please enter your url: ')
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# remove <script> tag
for s in soup(["script", "style"]):
    s.extract()

text = re.findall(r"\w+", soup.get_text().encode("utf-8"))

# remove all stop words and numbers
stopword = stopwords.words('english')

nostopword = []

for w in text:
    if not w in stopword and w.isalpha():
        nostopword.append(w)
print Counter(nostopword).most_common(100)  # count the top 100 occurrence words.
print

# make font color in word cloud gray
def grey_color(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)


print "please wait for few seconds..."

wordcloud = WordCloud(background_color='black',
                      stopwords=STOPWORDS,
                      max_words=100,
                      width=1800,
                      height=1400,
                      font_path='~/Amsdam Regular.ttf').generate(str(nostopword))

# Open a plot of the generated image.
plt.imshow(wordcloud.recolor(color_func=grey_color, random_state=3))
plt.axis("off")
plt.show()
