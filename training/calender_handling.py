
'''EG 1'''

'''SOLUTION 1'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://www.goibibo.com/')
# time.sleep(2)
#
# driver.find_element('xpath','//span[@class="logSprite icClose"]').click() #close the login
# time.sleep(3)
# driver.find_element('xpath','//span[text()="Departure"]').click()
# time.sleep(2)
#
# while True:
#     month = driver.find_element('xpath', '(//div[@class="DayPicker-Caption"])[1]')
#     print(month.text)
#     if month.text == 'November 2026':
#         driver.find_element('xpath', '(//p[text()="20"])[1]').click()   #select date
#         break
#     else:
#         driver.find_element('xpath', '//span[@aria-label="Next Month"]').click()   #click right arrow

#####################################################################################################
'''EG 2'''

'''SOLUTION 2'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://www.makemytrip.com/')
# driver.maximize_window()
# time.sleep(2)
# driver.find_element('xpath','//span[@class="commonModal__close"]').click()
# time.sleep(3)
# driver.find_element('xpath','//span[text()="Departure"]').click()
# time.sleep(3)
#
# while True:
#     try:
#         driver.find_element('xpath','//div[text()="September 2026"]/../..//p[text()="9"]').click()
#         break
#     except:
#         driver.find_element('xpath','//span[@aria-label="Next Month"]').click()

########OR#############

# def select_date(month ,date):
#     while True:
#         try:
#             driver.find_element('xpath', '//div[text()="{month}"]/../..//p[text()="{date}"]').click()
#             break
#         except:
#             driver.find_element('xpath', '//span[@aria-label="Next Month"]').click()
#
# select_date('September 2026',9)
