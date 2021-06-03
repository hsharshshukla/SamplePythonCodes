# import pywhatkit
# pywhatkit.sendwhatmsg('+918802545189', 'Test', 1, 17, 20)

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

jokes = ["Test1",
         "Test2"]

options = Options()
options.add_argument("--user-data-dir=C:\\Users\\Harsh\\AppData\Local\\Google\\Chrome\\User Data")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome('F:\SDE\drivers\chromedriver_win32\chromedriver', options=options)
driver.maximize_window()
driver.get('https://web.whatsapp.com')  # Already authenticated

time.sleep(9)

##################### Provide Recepient Name Here ###############################
obj = driver.find_element_by_xpath("//span[@title='bahu']")
obj.click()

for joke in jokes:
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(joke)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(3)

print("sent")
time.sleep(30)
driver.close()
