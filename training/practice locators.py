'''1.ID LOCATOR'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.saucedemo.com")
# time.sleep(2)
# driver.find_element("id","user-name").send_keys("standard_user")
# time.sleep(1)
# driver.find_element("id","password").send_keys("secret_sauce")
# time.sleep(1)
# driver.find_element("id","login-button").click()

########################################################################################

'''2. NAME LOCATOR'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.get('https://www.instagram.com/accounts/emailsignup/')
# time.sleep(2)
# driver.find_element("name","emailOrPhone").send_keys("suhana@gmail.com")
# time.sleep(1)
# driver.find_element("name","password").send_keys("suhana@123")
# time.sleep(1)
# driver.find_element("name","fullName").send_keys("FathimaSuhana")
# time.sleep(1)
# driver.find_element("name","username").send_keys("Fathima_Suhana")

#################################################################################

''' 3. CLASSNAME LOCATOR'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.facebook.com/r.php?entry_point=login")
# time.sleep(2)
# driver.find_element("class name","inputtext._58mg._5dba._2ph-").send_keys("Fathima")
# time.sleep(1)

#Here we use dots instead of space
#Here also multiple occurences drawback

#####################################################################################################

'''4. TAGNAME LOCATOR'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.get(r"C:\Users\faiza\PycharmProjects\Selenium_training\files\css_selector.html")
# time.sleep(2)
# driver.find_element("tag name","input").send_keys("Fathima")
# time.sleep(1)
# driver.find_element("tag name","input").send_keys("Adil")

##############################################################################################

'''5. LINKTEXT LOCATOR'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.myntra.com/")
# time.sleep(2)
# driver.find_element("link text","Men").click()
# time.sleep(1)
# driver.find_element("link text","Kids").click()
# time.sleep(1)

##############################################################################################

'''6. PARTIAL LINKTEXT LOCATOR'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
# driver.find_element("partial link text","Books").click()
# time.sleep(1)
# driver.find_element("partial link text","Computer").click()
# time.sleep(1)
# driver.find_element("partial link text","Electronics").click()

##################################################################################

'''7. CSS SELECTOR LOCATOR'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://in.indeed.com/')
# time.sleep(2)
# driver.find_element('css selector','input[id="text-input-what"]').send_keys('Software Engineer')
# time.sleep(1)
# driver.find_element('css selector','input[id="text-input-where"]').send_keys('Bengaluru')
# time.sleep(1)
# driver.find_element('css selector','button[type="submit"]').click()

#############################################################################################################

'''8.XPATH'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com')
# time.sleep(2)
#
# driver.find_element('xpath','html/body/div/div/div[2]/div/div/div/form/div[1]/input').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('xpath','html/body/div/div/div[2]/div/div/div/form/div[2]/input').send_keys('secret_sauce')

###################################################################################################################

'''USING ATTRIBUTE NAME AND ATTRIBUTE VALUE'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get('https://www.olacabs.com/')
# time.sleep(2)
# driver.find_element('xpath','//input[@id="textbox1"]').send_keys('Whitefield')
# time.sleep(1)
# driver.find_element('xpath','(//li[@class="item"])[2]').click()
# time.sleep(1)
# driver.find_element('xpath','//input[@placeholder="Enter Location"]').send_keys('Madiwala')
# time.sleep(1)
# driver.find_element('xpath','(//li[@class="item"])[14]').click()
# time.sleep(1)
# driver.find_element('xpath','//button[@class="search_btn"]').click()

##################################################################################

'''USING TEXT'''
# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.get('https://www.snapdeal.com/')
# time.sleep(2)
# driver.find_element('xpath','''//div[text()="Men's Fashion"]''').click()
# time.sleep(1)
# driver.find_element('xpath','//div[text()="Home & Kitchen"]').click()

################################################################################

'''USING CONTAINS'''
# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.get("https://selectorshub.com/")
# time.sleep(2)
# driver.find_element('xpath','//span[contains(text(),"Products")]').click()
# time.sleep(1)
# driver.find_element('xpath','//span[contains(text(),"Resources")]').click()

##########################################################################################

'''USING DEPENDENT AND INDEPENDENT XPATH'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.get("https://in.tradingview.com/")
# time.sleep(2)
# driver.find_element('xpath','//span[text()="Search"]').click()
# time.sleep(1)
# driver.find_element('xpath','//input[@type="search"]').send_keys("adanipower")
# time.sleep(1)
# driver.find_element('xpath','(//button[@aria-label="Search"])[3]').click()
# time.sleep(1)
# adanipower=driver.find_element('xpath','(//span[text()="ADANIPOWER"])[4]/../../..//span[@class="priceWrapper-qWcO4bp9"]')
# print(adanipower.text)

