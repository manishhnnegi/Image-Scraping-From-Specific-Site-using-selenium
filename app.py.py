#imge extraction from "https://uttarakhandtourism.gov.in"
from selenium import webdriver
import time
import requests
from creatfilepath2 import *
from creatfold import *



def serach_url(imag_count, driverpath):
    driver = webdriver.Chrome(executable_path= driverpath)
    url = "https://uttarakhandtourism.gov.in"
    driver.get(url)
    time.sleep(5)
    d =driver.find_elements_by_xpath('//img[@typeof="Image"]')
    t =set()
    max_count = len(d)
    if img_count < max_count:
        for i in range(img_count):
            t.add(d[i].get_attribute('src'))
    else:
        print("out of range")
    return t

def search_img(img_count, driverpath):
    folder_nm = "uttarakhand"
    keyword = 'uk'
    autofolder_creation(folder_nm)
    t = serach_url(img_count, driverpath)
    for i in t:
        url1 = i
        image_content = requests.get(url1).content
        time.sleep(5)
        path = autofile_path(keyword, folder_nm)
        h = open(path,'wb')
        h.write(image_content)
        h.close()
        print("the downloded succefully")







img_count = 4
driverpath = 'E:\IMZ\chromedriver.exe'
search_img(img_count, driverpath)