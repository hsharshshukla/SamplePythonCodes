import numbers
import time
import beepy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

#function for sending message
def send_msg(city):
    beepy.beep(sound=6)
    msg = city + " - Vaccine Slot Open please hurry!"

    options = Options()
    options.add_argument("--user-data-dir=C:\\Users\\Harsh\\AppData\Local\\Google\\Chrome\\User Data")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome('F:\SDE\drivers\chromedriver_win32\chromedriver', options=options)
    driver.maximize_window()
    driver.get('https://web.whatsapp.com')  # Already authenticated

    time.sleep(20)

    ##################### Provide Recepient Name Here ###############################
    # obj = driver.find_element_by_xpath("//span[@title='bahu']")
    obj = driver.find_element_by_xpath("//span[@title='bahu']")

    obj.click()

    for xi in range(2):
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(msg)
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
        time.sleep(3)

    time.sleep(30)
    driver.close()


#perform slot check
def slot_check_bbmp():
    driver = webdriver.Firefox("C:\\Users\\Harsh\\Downloads\\geckodriver-v0.29.1-win64")
    driver.get("https://www.cowin.gov.in/home")
    driver.find_element_by_xpath("//label/div").click()
    driver.find_element_by_xpath("//mat-select[@id='mat-select-0']/div/div[2]/div").click()
    driver.find_element_by_xpath("//mat-option[@id='mat-option-16']/span").click() #Karnataka
    driver.find_element_by_xpath("//div[@id='mat-select-value-3']/span").click()  #BBMP
    driver.find_element_by_xpath("//mat-option[@id='mat-option-40']/span").click()
    driver.find_element_by_xpath("//div[3]/button").click()
    driver.find_element_by_xpath("//div[3]/div/div/label").click()

    obj = driver.find_elements_by_xpath("//div[contains(@class,'slots-box')]")

    i=0
    flag=''
    for o in obj:
        slot_count = o.text.partition('\n');
        slot = slot_count[0]

        try:
            a = int(slot)
            flag ='x'
            break
        except:
            pass

    if flag=='x':
        beepy.beep(sound=6)
        count =2
        while (count>0):
            send_msg('BBMP')
            count -=1

    time.sleep(20)
    driver.quit()

#Bangalore Urban
def slot_check_burban():
    driver = webdriver.Firefox("C:\\Users\\Harsh\\Downloads\\geckodriver-v0.29.1-win64")
    driver.get("https://www.cowin.gov.in/home")
    driver.find_element_by_xpath("//label/div").click()
    driver.find_element_by_xpath("//mat-select[@id='mat-select-0']/div/div[2]/div").click()
    driver.find_element_by_xpath("//mat-option[@id='mat-option-16']/span").click() #Karnataka
    driver.find_element_by_xpath("//div[@id='mat-select-value-3']/span").click()  #BBMP
    driver.find_element_by_xpath("//mat-option[@id='mat-option-39']/span").click()
    driver.find_element_by_xpath("//div[3]/button").click()
    driver.find_element_by_xpath("//div[3]/div/div/label").click()

    obj = driver.find_elements_by_xpath("//div[contains(@class,'slots-box')]")

    flag=''
    for o in obj:
        # print(i)
        slot_count = o.text.partition('\n');
        slot = slot_count[0]

        try:
            a = int(slot)
            flag ='x'

            break
        except:
            pass

    if flag=='x':
        beepy.beep(sound=6)
        count =2
        while (count>0):
            send_msg('Bangalore Urban')
            count -=1

    time.sleep(30)
    driver.quit()

#Bangalore Rural
def slot_check_brural():
    driver = webdriver.Firefox("C:\\Users\\Harsh\\Downloads\\geckodriver-v0.29.1-win64")
    driver.get("https://www.cowin.gov.in/home")
    driver.find_element_by_xpath("//label/div").click()
    driver.find_element_by_xpath("//mat-select[@id='mat-select-0']/div/div[2]/div").click()
    driver.find_element_by_xpath("//mat-option[@id='mat-option-16']/span").click() #Karnataka
    driver.find_element_by_xpath("//div[@id='mat-select-value-3']/span").click()  #BBMP
    driver.find_element_by_xpath("//mat-option[@id='mat-option-38']/span").click()
    driver.find_element_by_xpath("//div[3]/button").click()
    driver.find_element_by_xpath("//div[3]/div/div/label").click()

    obj = driver.find_elements_by_xpath("//div[contains(@class,'slots-box')]")

    flag=''
    for o in obj:
        slot_count = o.text.partition('\n');
        slot = slot_count[0]
        try:
            a = int(slot)
            flag = 'x'

            break
        except:
            pass

    if flag=='x':
        beepy.beep(sound=6)
        count =2
        while (count>0):
            send_msg('Bangalore Rural')
            count -=1

    time.sleep(30)
    driver.quit()

#Ghaziabad
def slot_check_gzb():
    #Date check
    driver = webdriver.Firefox("C:\\Users\\Harsh\\Downloads\\geckodriver-v0.29.1-win64")
    driver.get("https://www.cowin.gov.in/home")
    driver.find_element_by_xpath("//label/div").click()
    driver.find_element_by_xpath("//mat-select[@id='mat-select-0']/div/div[2]/div").click()
    driver.find_element_by_xpath("//mat-option[@id='mat-option-34']/span").click() #U.P
    driver.find_element_by_xpath("//div[@id='mat-select-value-3']/span").click()
    driver.find_element_by_xpath("//mat-option[@id='mat-option-66']/span").click() #Ghaziabad
    driver.find_element_by_xpath("//div[3]/button").click()
    driver.find_element_by_xpath("//div[2]/label").click()

    obj = driver.find_elements_by_xpath("//div[contains(@class,'slots-box')]")

    flag=''
    for o in obj:
        slot_count = o.text.partition('\n');
        slot = slot_count[0]
        try:
            a = int(slot)
            flag ='x'
            break
        except:
            pass

    if flag=='x':
        count =2
        while (count>0):
            send_msg('Ghaziabad')
            count -=1

    time.sleep(30)
    driver.quit()

# slot_check_brural()
# slot_check_burban()
# slot_check_bbmp()
slot_check_gzb()
