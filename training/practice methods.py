'''CALENDER HANDLING'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.makemytrip.com/")
# driver.maximize_window()
# time.sleep(2)
# driver.find_element('xpath','//span[@class="commonModal__close"]').click()
# time.sleep(3)
# driver.find_element('xpath','//span[text()="Departure"]').click()
# time.sleep(2)
# while True:
#     try:
#         driver.find_element('xpath','//div[text()="April 2026"]/../..//p[text()="25"]').click()
#         break
#     except:
#         driver.find_element('xpath','//span[@aria-label="Next Month"]').click()

########################################################################################################

'''READING TABLE'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
# for r in range(2,8):
#     for c in range(1,5):
#         data=driver.find_element('xpath',f'//table[@name="BookTable"]//tr[{r}]/td[{c}]')
#         print(data.text,end='\t\t')
#     print()

# for r in range(2,7):
#     for c in range(1,4):
#         data2=driver.find_element('xpath',f'//table[@id="productTable"]//tr[{r}]/td[{c}]')
#         print(data2.text,end='\t\t')
#     print()
###################################################################################################

'''FIND ELEMENTS'''
# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)

##To print the elements present in the footer

# footer_elements=driver.find_elements('xpath','//div[@class="footer-menu-wrapper"]//a')
# # print(footer_elements)
# for ele in footer_elements:
#     print(ele.text)

##To print the elements in the categories of the app

# categories=driver.find_elements('xpath','//div[@class="block block-category-navigation"]//a')
# # print(categories)
# for ele in categories:
#     print(ele.text)

######################################################################################################

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
# popular_searches=driver.find_elements('xpath','//div[@class="desktop-popularSearch"]//a')
# for ele in popular_searches:
#     print(ele.text)

###################################################################################################'

'''GETTER METHOD'''
# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.get('https://www.myntra.com/')
# time.sleep(2)
# beauty=driver.find_element('xpath','(//a[text()="Beauty"])[1]')
# print(beauty.get_attribute("href"))
# print(beauty.get_attribute("style"))
# print(beauty.text)
# print(beauty.get_dom_attribute("style"))
# print(beauty.get_dom_attribute("class"))

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.facebook.com/r.php?entry_point=login")
# time.sleep(2)
# # firstname=driver.find_element("name","firstname")
# # print(firstname.tag_name)
# signup=driver.find_element("name","websubmit")
# print(signup.tag_name)

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.facebook.com/r.php?entry_point=login")
# time.sleep(2)
# firstname=driver.find_element("name","firstname")
# print(firstname.aria_role)
# gender=driver.find_element("id","sex")
# print(gender.aria_role)


# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
# search=driver.find_element('xpath','//input[@class="button-1 search-box-button"]')
# print(search.accessible_name)
# vote=driver.find_element("id","vote-poll-1")
# print(vote.accessible_name)

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.get('https://www.myntra.com/')
# time.sleep(2)
# beauty=driver.find_element('xpath','(//a[text()="Beauty"])[1]')
# print(beauty.value_of_css_property('font-weight'))
# print(beauty.value_of_css_property('letter-spacing'))

########################################################################################

'''PARENT CHILD'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
# driver.find_element('xpath','//div[@class="block block-category-navigation"]//a[contains(text(),"Books")]').click()


'''IFRAME'''


# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# driver=webdriver.Chrome(opts)
# ac=ActionChains(driver)
#
# driver.get("https://www.linkedin.com")
# time.sleep(2)
#
# google_frame=driver.find_element('xpath','//iframe[@title="Sign in with Google Button"]')
# time.sleep(2)
#
# driver.switch_to.frame(google_frame)
# time.sleep(2)
#
# driver.find_element('xpath','//span[text()="Continue with Google"]').click()
# time.sleep(2)
#
# driver.switch_to.parent_frame()
# time.sleep(2)
#
# ref_ele=driver.find_element('xpath','//h2[contains(text(),"Join your colleagues")]')
# ac.scroll_to_element(ref_ele).perform()
# time.sleep(2)
#
# youtube_frame=driver.find_element('xpath','//iframe[@title="Gayatri Iyer: In it to chase my dream | #InItTogether"]')
# time.sleep(2)
#
# driver.switch_to.frame(youtube_frame)
# time.sleep(2)
#
# driver.find_element('xpath','//button[@title="Play"]').click()
# time.sleep(2)
#
# driver.switch_to.parent_frame()
# time.sleep(2)

#---------------------------------------------------------------------------------------------------

# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# driver=webdriver.Chrome(opts)
# ac=ActionChains(driver)
# wait_=WebDriverWait(driver,10)
#
#
# driver.get("https://www.linkedin.com")
# time.sleep(2)
#
# def switch_to_frame(loc_name,loc_value):
#     return wait_.until(EC.frame_to_be_available_and_switch_to_it((loc_name,loc_value)))
#
# def switch_to_parent():
#     return driver.switch_to.parent_frame()
#
# switch_to_frame('xpath','//iframe[@title="Sign in with Google Button"]')
# time.sleep(2)
#
#
# driver.find_element('xpath','//span[text()="Continue with Google"]').click()
# time.sleep(2)
#
# switch_to_parent()
# time.sleep(2)
#
# ref_ele=driver.find_element('xpath','//h2[contains(text(),"Join your colleagues")]')
# ac.scroll_to_element(ref_ele).perform()
# time.sleep(2)
#
# switch_to_frame('xpath','//iframe[@title="Gayatri Iyer: In it to chase my dream | #InItTogether"]')
# time.sleep(2)
#
#
# driver.find_element('xpath','//button[@title="Play"]').click()
# time.sleep(2)
#
# switch_to_parent()
# time.sleep(2)

########################################################################################################

import xlrd

path=r'C:\Users\faiza\PycharmProjects\Selenium_training\files\a13.xlsx'
workbook=xlrd.open_workbook(path)

worksheet=workbook.sheet_by_name("personal_info")

rows=worksheet.get_rows()
# for ele in rows:
#     print(ele)


# header=next(rows)
# print(header)

# i=0
#
# for ele in rows:
#     if i==2:
#         break
#     print(ele)
#     i=i+1


# i=1
#
# for ele in rows:
#     if i==4:
#         print(ele)
#         break
#     i=i+1


# for ele in rows:
#     print(ele[0].value,ele[1].value,ele[2].value,ele[3].value)


# for ele in rows:
#     print(ele[0].value)


# data={}
# header=next(rows)
# for ele in rows:
#     data[ele[0].value]=(ele[1].value,ele[2].value,ele[3].value)
# print(data)





















