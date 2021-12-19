from bs4 import BeautifulSoup
import requests
import lxml

url = "https://www.ynet.co.il/home/0,7340,L-8,00.html"

response = requests.get(url)
web_page = response.text

soup = BeautifulSoup(web_page, "lxml")

headtitle = soup.find(name="h1", class_="slotTitle").get_text()

print(headtitle[::-1])
print("or")
print(headtitle)
print("-----------------------------------------------------------------------")
print("I did both way because on different interpreter hebrew print in reverse")