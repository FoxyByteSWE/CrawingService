import pandas as pd
import time
import re
import os
import csv
import json
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriverDirectory = "C:/Users/marco/Desktop/FoxyByte/Crawler/chromedriver.exe"  #EDIT
profileDirectory = "C:/Users/marco/Desktop/FoxyByte/Crawler/Profile"	#EDIT

def buildWebDriver():
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_experimental_option("useAutomationExtension", False)
	chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
	chrome_options.add_argument("user-data-dir=" + profileDirectory)

	driver = webdriver.Chrome(chromedriverDirectory, options=chrome_options)
	return driver



def getLocationPageBySearchBar(locationName, driver):
	driver.get("https://www.instagram.com/")
	time.sleep(3)

	element = WebDriverWait(driver, 20).until(
	EC.element_to_be_clickable((By.XPATH, "//input[contains(@class,'XTCLo')]")))
 
	time.sleep(5)
	driver.execute_script("arguments[0].click();", element)
	time.sleep(5)
	element.send_keys(locationName)
	time.sleep(2)

	url_array = driver.find_elements_by_css_selector(".-qQT3")
	
	for url in url_array:
		if 'explore/locations' in str(url.get_attribute('href')):
			print(url.get_attribute('href'))	
			return str(url.get_attribute('href'))




def crawlLocation(locationURL, driver):
	driver.get(locationURL)
	time.sleep(3)

	screen_height = driver.execute_script("return window.screen.height;")
	i = 1	
	while True:
		driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
		i += 1
		time.sleep(3)
		scroll_height = driver.execute_script("return document.body.scrollHeight;")  
		if (screen_height) * i > scroll_height or i>20:
			break 
	
	posts = driver.find_elements_by_css_selector(".FFVAD")
	src_data_array=[]
	for data in posts:
		src_data_array.append(data.get_attribute('src'))
	
	post_src_array=[]
	for src in src_data_array:
		post_src_array.append(src)
	
	return post_src_array
		

















def getComments(url):
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_experimental_option("useAutomationExtension", False)
	chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
	chrome_options.add_argument("user-data-dir=C:/Users/marco/Desktop/FoxyByte/Crawler/Profile"); #edit 

	driver = webdriver.Chrome("C:/Users/marco/Desktop/FoxyByte/Crawler/chromedriver.exe", options=chrome_options) #edit
	driver.get(url)
	time.sleep(5)

	texts_list = []
	texts = driver.find_elements_by_css_selector('.MOdxS ')
	print(len(texts))
	for txt in texts:
		texts_list.append(txt.text)
		print("Text: ",txt.text)

		











#################################################################

def main():


	getComments("https://www.instagram.com/p/Cd52IzArohl/")
#	
#	locationName=input("Please Input the Location Name: ")
#	driver = buildWebDriver()
#
#	url = getLocationPageBySearchBar(locationName, driver)
#	posts_array = crawlLocation(url, driver)
#
#
#	location_dictionary={}
#	location_dictionary[locationName] = posts_array
#
#	jsonDump = json.dumps(location_dictionary)
#	with open("locationsposts.json", "a") as outfile:
#		outfile.write(jsonDump)
#
#	i=1
#	for url in posts_array:
#		print(url)
#		i=i+1
#
#	print("Got "+str(i)+"posts")
#
################################################################

if __name__ == "__main__":
    main()