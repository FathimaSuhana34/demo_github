'''Iniializing application'''
#import time
#from selenium import webdriver
#opts=webdriver.ChromeOptions()
#opts.add_experimental_option("detach",True)
#driver=webdriver.Chrome(opts)


'''Launching application'''
#driver.get("https://www.saucedemo.com")
#time.sleep(2)


'''Locating Webelement'''
#username=driver.find_element("id","user-name")
#print(username)

#password=driver.find_element("id","password")
#print(password)

#################################################################################

'''EG 1'''
#import time
#from selenium import webdriver
#opts=webdriver.ChromeOptions()
#opts.add_experimental_option("detach",True)
#driver=webdriver.Chrome(opts)


#driver.get("https://www.saucedemo.com")
#time.sleep(2)

'''Interacting with webelement'''
#driver.find_element("id","user-name").send_keys("standard_user")
#time.sleep(1)
#driver.find_element("id","password").send_keys("secret_sauce")
#time.sleep(1)
#driver.find_element("id","login-button").click()
#time.sleep(3)
#driver.find_element("id","react-burger-menu-btn").click()
#time.sleep(2)
#driver.find_element("id","logout_sidebar_link").click()


###############################################################################

'''EG 2'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)

# driver.get("https://demowebshop.tricentis.com/register")
# time.sleep(2)

# driver.find_element("id","gender-female").click()
# time.sleep(1)
# driver.find_element("id","FirstName").send_keys("Fathima")
# time.sleep(1)
# driver.find_element("id","LastName").send_keys("Suhana")
# time.sleep(1)
# driver.find_element("id","Email").send_keys("fathima@gmail.com")
# time.sleep(1)
# driver.find_element("id","Password").send_keys("fathima@12345")
# time.sleep(1)
# driver.find_element("id","ConfirmPassword").send_keys("fathima@12345")