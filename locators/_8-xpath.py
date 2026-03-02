
'''EG 1'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\faiza\PycharmProjects\Selenium_training\files\css_selector.html')
# time.sleep(2)
# driver.find_element('xpath','html/body/table[2]/tbody/tr[1]/td/input').send_keys('Fathima')
# time.sleep(1)
# driver.find_element('xpath','html/body/table[2]/tbody/tr[2]/td/input').send_keys('fathima@123')


########################################################################################################

'''EG 2'''
#
# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('xpath','html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('xpath','html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('xpath','html/body/div/div/div[2]/div[1]/div/div/form/input').click()


#############################################################################################
'''Locating webelement using attribute name and attribute value'''

'''EG 1'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://www.instagram.com/')
# time.sleep(2)
#
# driver.find_element('xpath','//input[@aria-label="Phone number, username or email address"]').send_keys('Fathima')
# time.sleep(1)
# driver.find_element('xpath','//input[@aria-label="Password"]').send_keys('fathima@123')
# time.sleep(1)
# driver.find_element('xpath','//button[@type="submit"]').click()

####################################################################################################

'''EG 2'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com')
# time.sleep(2)
#
# driver.find_element('xpath','//input[@data-test="username"]').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('xpath','//input[@data-test="password"]').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('xpath','//input[@id="login-button"]').click()
# time.sleep(3)
# driver.find_element('xpath','//button[@id="react-burger-menu-btn"]').click()
# time.sleep(2)
# driver.find_element('xpath','//a[@data-test="logout-sidebar-link"]').click()

###########################################################################################

'''GROUP INDEXING'''

'''EG 1'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://www.olacabs.com/')
# time.sleep(2)
#
# driver.find_element('xpath','//input[@id="textbox1"]').send_keys('Baswangudi')
# time.sleep(1)
# driver.find_element('xpath','(//li[@class="item"])[1]').click()
# time.sleep(1)
# driver.find_element('xpath','//input[@id="destination_location"]').send_keys('Whitefield')
# time.sleep(1)
# driver.find_element('xpath','(//li[@class="item"])[14]').click()
# time.sleep(1)
# driver.find_element('xpath','//button[@class="search_btn"]').click()

######################################################################################################

'''EG 2'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(1)
# driver.find_element('xpath','(//input[@type="text"])[1]').send_keys('Fathima')
# time.sleep(1)
# driver.find_element('xpath','(//input[@type="text"])[2]').send_keys('Suhana')
# time.sleep(1)
# driver.find_element('xpath','(//input[@type="text"])[5]').send_keys('fathima@gmail.com')

#################################################################################################

'''Locating webelement using text'''

'''EG 1'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://www.snapdeal.com/')
# time.sleep(3)
#
# driver.find_element('xpath','''//div[text()="Men's Fashion"]''').click()
# time.sleep(1)
# driver.find_element('xpath','//div[text()="Home & Kitchen"]').click()

###########################################################################################

#Another type of Xpath
'''Contains:To locate the webelement using partial text of any tagname'''

'''EG 1'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://selectorshub.com/')
# time.sleep(2)
#
# driver.find_element('xpath','//span[contains(text(),"Products")]').click()
# time.sleep(1)
# driver.find_element('xpath','//span[contains(text(),"Pro Plans")]').click()
# time.sleep(1)

####################################################################################

'''EG 2'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://www.kushals.com/')
# time.sleep(2)
#
# driver.find_element('xpath','(//a[contains(text(),"Bangles")])[2]').click()
# time.sleep(1)
# driver.find_element('xpath','(//a[contains(text(),"Earrings")])[2]').click()
# time.sleep(1)
# driver.find_element('xpath','(//a[contains(text(),"92.5 Silver")])[5]').click()

#########################################################################################

'''DEPENDENT AND INDEPENDENT XPATH '''

'''EG 1'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)

# driver.get(r'C:\Users\faiza\PycharmProjects\Selenium_training\files\demo.html')
# time.sleep(2)
#
# driver.find_element('xpath','//td[text()="Python"]/..//input[@type="checkbox"]').click()
# time.sleep(1)
# driver.find_element('xpath','//td[text()="Java"]/..//input[@name="download"]').click()

###############################################################################################

'''EG 2'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\faiza\PycharmProjects\Selenium_training\files\demo.html')
# time.sleep(2)
#
# driver.find_element('xpath','//td[text()="Windows"]/..//a[text()="Download"]').click()
# time.sleep(1)
#
# ##To include version
# driver.find_element('xpath','//td[text()="Windows"]/..///td[text()="3.140"]/../a[text="Download"]').click()


###############################################################################################################

'''EG 3'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://www.python.org/')
# time.sleep(1)
#
# driver.find_element('xpath','//a[text()="Downloads"]').click()
# time.sleep(2)
# driver.find_element('xpath','//a[text()="Python 3.13.10"]/../..//a[text()="Release notes"]').click()

#########################################################################################################

'''EG 4'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://in.tradingview.com/')
# time.sleep(2)
#
# driver.find_element('xpath','//span[text()="Search"]').click()
# time.sleep(2)
# driver.find_element('xpath','//input[@type="search"]').send_keys('adanipower')
# time.sleep(2)


##########################################################################################

'''EG 5'''

# import time
# from selenium import webdr
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://www.iforex.in/')
# time.sleep(2)
#
# driver.find_element('xpath','//h2[text()="iFOREX AI"]/')
# driver.find_element('xpath','//div[@id="ai-chat-close"]').click()

####################################################################################

'''PARENT CHILD RELATIONSHIP'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# driver.find_element('xpath','//div[@class="block block-category-navigation"]//a[contains(text(),"Books")]').click()
# time.sleep(1)
# driver.find_element('xpath','//div[@class="block block-category-navigation"]//a[contains(text(),"Apparel & Shoes")]').click()

######################################################################################################################################

'''CHILD PARENT RELATIONSHIP'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://www.instagram.com/')
# time.sleep(2)
#
# driver.find_element('xpath','//input[@name="username"]/..')      ##goes back to immediate parent
#
# #To locate the immediate parent
# driver.find_element('xpath','//input[@name="username"]/parent::label')

####################################################################################################

'''SIBLINGS'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://www.python.org/downloads/')
# time.sleep(2)
#
# #preceding sibling
# driver.find_element('xpath','(//span[text()="Oct. 7, 2025"])[1]/preceding-sibling::span')
#
# #incase of multiple preceding siblings,we can do indexing
# driver.find_element('xpath','(//span[text()="Oct. 7, 2025"])[1]/preceding-sibling::span[1]')
#
# #following sibling
# driver.find_element('xpath','(//span[text()="Oct. 7, 2025"])[1]/following-sibling::span')
#
# ##incase of multiple following siblings,we can do indexing
# driver.find_element('xpath','(//span[text()="Oct. 7, 2025"])[1]/following-sibling::span[1]')

#################################################################################################

'''ANCESTOR'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://www.instagram.com/")
# time.sleep(2)
#
# driver.find_element('xpath','//input[@name="username"]/ancestor::div')
#
# #incase of multiple occurences,we can do indexing
# driver.find_element('xpath','//input[@name="username"]/ancestor::div[n]')

###################################################################################

'''DESCENDANT/ANY CHILD'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://www.instagram.com/")
# time.sleep(2)
#
# driver.find_element('xpath','//form[@id="loginForm"]/descendant::input')
#
# #incase of multiple occurence, we can do indexing
# driver.find_element('xpath','//form[@id="loginForm"]/descendant::input[2]')

######################################################################################################

'''ABOVE'''

# import time
# from selenium import webdriver
# from selenium.webdriver.support.relative_locator import locate_with
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# ele=driver.find_element('xpath','//td[text()="Learn Java"]')
# ele1=driver.find_element(locate_with('tag name','td').above(ele))
# print(ele1.text)

###########################################################################################################

'''BELOW'''

# import time
# from selenium import webdriver
# from selenium.webdriver.support.relative_locator import locate_with
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# ele=driver.find_element('xpath','//td[text()="Master In Java"]')
# ele1=driver.find_element(locate_with('tag name','td').below(ele))
# print(ele1.text)

###############################################################################################

'''TO_LEFT_OF'''

# import time
# from selenium import webdriver
# from selenium.webdriver.support.relative_locator import locate_with
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# ele=driver.find_element('xpath','(//td[text()="Amit"])[2]')
# ele1=driver.find_element(locate_with('tag name','td').to_left_of(ele))
# print(ele1.text)

########################################################################################################

'''TO_RIGHT_OF'''

# import time
# from selenium import webdriver
# from selenium.webdriver.support.relative_locator import locate_with
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# ele=driver.find_element('xpath','(//td[text()="Amit"])[2]')
# ele1=driver.find_element(locate_with('tag name','td').to_right_of(ele))
# print(ele1.text)

































