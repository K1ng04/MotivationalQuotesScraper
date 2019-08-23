from bs4 import BeautifulSoup
import requests
from random import choice

res = requests.get("http://wisdomquotes.com/motivational-quotes/")
soup = BeautifulSoup(res.text, "html.parser")
x = soup.find_all('blockquote')
y = [quotes.find('p').text for quotes in x]
print(choice(y))  # - -> List Comp use is possible
# for quotes in x:
#     z = quotes.find('p').text
#     print(z)
