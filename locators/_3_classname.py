

'''EG 1'''

# import time
# from  selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# driver.find_element("class name","ico-register").click()
# time.sleep(1)
# driver.find_element("class name","ico-login").click()
# time.sleep(1)
# driver.find_element("class name","cart-label").click()

################################################################################

'''EG 2'''

# import time
# from  selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\faiza\PycharmProjects\Selenium_training\files\css_selector.html')
# time.sleep(2)
#
# driver.find_element("class name","first_row").send_keys("Fathima")
# time.sleep(1)
# driver.find_element("class name","first_row").send_keys("Suhana")
# time.sleep(1)
# driver.find_element("class name","first_row").send_keys("Raseena")

##Both values will be filled in the first textbox
## Because whenever we are having multiple occurences,class name locator will always consider the first occurence

####################################################################################################################

'''EG 3'''

# import time
# from  selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://www.facebook.com/r.php?entry_point=login")
# time.sleep(2)
#
# driver.find_element("class name","inputtext _58mg _5dba _2ph-").send_keys("Fathima")
# time.sleep(1)

##    NoSuchElementException
##Because class name locator cannot recognize the spaces we have in the value of the class attribute

####################################################################################################

#To overcome the above issues , we wil replace the space with dot(.)

# import time
# from  selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://www.facebook.com/r.php?entry_point=login")
# time.sleep(2)
#
# driver.find_element("class name","inputtext._58mg._5dba._2ph-").send_keys("Fathima")
# time.sleep(1)






























































