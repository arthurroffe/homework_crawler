# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 04:57:57 2022

@author: 88698
"""

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests 
from bs4 import BeautifulSoup as bs
import time
from selenium.webdriver.support.select import Select
import os
'''
基本動態爬蟲，使用chrome
'''
url = "https://plvr.land.moi.gov.tw/DownloadOpenData"

options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome("./chromedriver",chrome_options=options)
chrome.get(url)
#點選非本期下載
tab_button = chrome.find_element_by_id("ui-id-2")
tab_button.click()
time.sleep(2)
#選擇年季
post_date = chrome.find_element_by_id("historySeason_id")
post_date.click()
Select(post_date).select_by_value("108S2")
post_date.click()
time.sleep(1)
#選擇CSV
fileformat = chrome.find_element_by_id("fileFormatId")
Select(fileformat).select_by_value("csv")
fileformat.click()
time.sleep(1)
#選擇進階下載
downloadtype = chrome.find_element_by_id("downloadTypeId2")
downloadtype.click()
time.sleep(1)
#點選縣市
chrome.find_element_by_xpath("//input[@value='A_lvr_land_A']").click()
chrome.find_element_by_xpath("//input[@value='B_lvr_land_A']").click()
chrome.find_element_by_xpath("//input[@value='E_lvr_land_A']").click()
chrome.find_element_by_xpath("//input[@value='F_lvr_land_A']").click()
chrome.find_element_by_xpath("//input[@value='H_lvr_land_A']").click()
time.sleep(1)
#點選下載
chrome.find_element_by_id("downloadBtnId").click()


