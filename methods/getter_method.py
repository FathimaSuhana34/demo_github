'''1.GET_ATTRIBUTE'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
# home=driver.find_element('xpath','(//a[text()="Home"])[1]')
# print(home.get_attribute("href"))
# print(home.get_attribute("data-group"))

#####################################################################################

'''2.TEXT'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# home=driver.find_element('xpath','(//a[text()="Home"])[1]')
# print(home.text)

###############################################################################

'''3.GET_DOM_ATTRIBUTE'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
# home=driver.find_element('xpath','(//a[text()="Home"])[1]')
# print(home.get_dom_attribute("href"))
#
# men=driver.find_element('xpath','//a[@data-group="men"]')
# print(men.get_dom_attribute("class"))

################################################################################

'''4.TAG_NAME'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://www.facebook.com/r.php?entry_point=login")
# time.sleep(2)
# firstname=driver.find_element("name","firstname")
# print(firstname.tag_name)
#
# signup=driver.find_element("name","websubmit")
# print(signup.tag_name)

###################################################################################

'''5.AREA_ROLE'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://www.facebook.com/r.php?entry_point=login")
# time.sleep(2)
# firstname=driver.find_element("name","firstname")
# print(firstname.aria_role)
#
# gender=driver.find_element("name","sex")
# print(gender.aria_role)
#
# account=driver.find_element("link text","Already have an account?")
# print(account.aria_role)

####################################################################################

'''6.ACCESSIBLE_NAME'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# searchbox=driver.find_element('xpath','//input[@class="button-1 search-box-button"]')
# print(searchbox.accessible_name)
#
# subscribe=driver.find_element('xpath','//input[@class="button-1 newsletter-subscribe-button"]')
# print(subscribe.accessible_name)
#
# logo=driver.find_element('xpath','//img[@alt="Tricentis Demo Web Shop"]')
# print(logo.accessible_name)

#####################################################################################################

'''7.VALUE_CSS_PROPERTY'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
# home=driver.find_element('xpath','(//a[text()="Home"])[1]')
# print(home.value_of_css_property("font-size"))      ##14px
# print(home.value_of_css_property("font-style"))     ##normal
#
# beauty=driver.find_element('xpath','//a[@data-group="beauty"]')
# print(beauty.value_of_css_property("padding"))

########################################################################################

'''8.SCREENSHOT'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# ##Takes screenshot of the entire page
# driver.save_screenshot("myn.png")
#
# ## To take the screenshot of th web element
# home=driver.find_element('xpath','(//a[text()="Home"])[1]')
# home.screenshot("home.png")






































































