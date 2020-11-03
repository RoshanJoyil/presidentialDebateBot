from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://youtube.com")
print("You are currently on", driver.title)

#find the search quey's source code in inspect element and find it's variable name-- in this case it was "search_query"
search = driver.find_element_by_name("search_query")
search.send_keys("test")
search.send_keys(Keys.RETURN)


#makes the program wait until the element with ID "content" is on the screen
try:
    content = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "content"))
    )

    titles = driver.find_elements_by_tag_name("ytd-item-section-renderer")
    for title in titles:
        header = driver.find_element_by_id("video-title")
        print(header.text)
finally:
    driver.quit()

