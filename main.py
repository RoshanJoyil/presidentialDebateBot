from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://youtube.com")
print(driver.title)

#find the search quey's source code in inspect element and find it's variable name-- in this case it was "search_query"
search = driver.find_element_by_name("search_query")
search.send_keys("test")
search.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()