from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import credentials
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


options = Options()
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=options)

driver.get("https://www.facebook.com/")

email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "pass")

email.send_keys(credentials.email)
password.send_keys(credentials.password)
password.submit()

time.sleep(5)

driver.get("https://www.facebook.com/ETtodayMOVIE")

for i in range(20):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)

soup = BeautifulSoup(driver.page_source, "lxml")

posts = soup.find_all("div", {"class": "x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z"})

result = []
for post in posts:
    content = post.find("span", {
                        "class": "x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u x1yc453h"})
    result.append(content.getText())

print(result)
