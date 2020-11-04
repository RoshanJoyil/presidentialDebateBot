from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

header = {
    'authorization' : "" #PUT YOUR DISCORD AUTHORIZATION CODE HERE
}

url = "https://discord.com/api/v8/channels/ /messages" #PUT THE CHANNEL ID IN THE SPACE


PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.google.com/search?rlz=1C1CHBF_enUS911US911&sxsrf=ALeKk02cfz9VF_66lJgvGkC5KQWE7NN4jQ%3A1604506560650&ei=wNOiX6yiJ4KRgger6peYBA&q=who%27s+winning+the+election+right+now&oq=who%27s+winning+the+&gs_lcp=CgZwc3ktYWIQAxgCMgQIIxAnMgcIIxDJAxAnMg0IABCxAxCDARAUEIcCMggIABCxAxCDATIICAAQsQMQgwEyCAgAELEDEIMBMgIIADIICAAQsQMQgwEyAggAMgIIADoECAAQA1DTGljLHmCrOmgAcAB4AIABS4gBvwGSAQEzmAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=psy-ab")

main = driver.find_element_by_id("main")

curbid = 0
curtrump = 0

try:
    while True:
        num = 0
        votes = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "KyJnQd"))
        )
        ballot = driver.find_elements_by_class_name("rDMtnd")
        for i in ballot:
            if num % 2 == 0:
                if int(i.text) != int(curbid):
                    print(int(i.text))
                    curbid = int(i.text)
                    bid = "Biden has " + str(curbid)
                    payload = {
                        'content': bid
                    }
                    r = requests.post(url, data=payload, headers=header)
                num += 1
            else:
                if int(i.text) != int(curtrump):
                    print(int(i.text))
                    curtrump = int(i.text)
                    trumpitis = "Trump has " + str(curtrump)
                    payload = {
                        'content': trumpitis
                    }
                    r = requests.post(url, data=payload, headers=header)
                num += 1

        time.sleep(60)
finally:
    driver.quit()
