
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup
import requests as re

# clue 1: always command(ctrl) + F. tjink of the right keywords and files
# look at css
# clue 3: look for {"finding", "good", "level", "3", "job"} in page 2 and 
# use what you find to get to page 3

url = re.get("https://hertie-scraping-website.vercel.app")
soup = BeautifulSoup(url.content, "html.parser")
nesting_1 = soup.find(id="nesting-1")
text_base = nesting_1.find_all(class_="text-base")
div_text_2 = "\n".join([item.get_text() for item in text_base])
print(div_text_2)
text_transparent = nesting_1.find(class_="text-transparent")
print(text_transparent.get_text())

first_span_9 = soup.find(class_="text-wrap flex justify-between")
flag_9_div = first_span_9.parent
flag_9_name = flag_9_div["id"]
print(flag_9_name)


text_wrap = soup.find(class_="text-wrap flex justify-between")
size_10_elements = text_wrap.find_all(class_="size-10")

for i, element in enumerate(size_10_elements):
    child = element.find('div')
    if i % 2 == 0:
        flag = child["class"][0]
        print(flag)
    else:
        flag = child["id"]
        print(flag)
        ###    
         

#    div = size.find("div")
#    try:
#        flag = div["class"]
#        print(flag.text.strip)
#    except:
#        flag = div["id"]
#        print(flag)







#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#driver.get("https://hertie-scraping-website.vercel.app")

#for i in range(len(flags)):
#    flags_list.append(flags[f].text)
#print(flags_list)

#print(driver.title)

#driver.close()
