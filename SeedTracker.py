#SeedTracker.py

#Needs these installs:
#pip install beautifulsoup4
#pip install -U selenium

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
	
def soupGet(driver, url):
	driver.get(url)
	return BeautifulSoup(driver.page_source, "lxml")	
	
def printStats(seedType, tree = False):
	if not tree:
		soup = soupGet(driver, "https://www.ge-tracker.com/item/"+seedType+"-seed")
	else:
		soup = soupGet(driver, "https://www.ge-tracker.com/item/"+seedType+"-tree-seed")
	offerPrice = soup.find("td", {"id": "item_stat_offer_price"}).text.strip()
	sellers = soup.find("td", {"id": "item_stat_selling"}).text.strip()
	soup = soupGet(driver, "https://www.ge-tracker.com/item/"+seedType+"-sapling")
	sellPrice = soup.find("td", {"id": "item_stat_sell_price"}).text.strip()
	buyers = soup.find("td", {"id": "item_stat_buying"}).text.strip()
	profit = int(sellPrice.replace(',', ''))-int(offerPrice.replace(',', ''))
	print("--"+seedType.capitalize()+" Seeds--")
	print("Approx Buy Price: "+offerPrice+" with "+sellers+" selling")
	print("Approx Sell Price: "+sellPrice+" with "+buyers+" buying")
	print("Approx Profit: "+str(profit))

driver = webdriver.Chrome()
driver.implicitly_wait(30)
printStats("willow")
printStats("maple")
printStats("yew")
printStats("pineapple")
printStats("papaya", True)

driver.close()