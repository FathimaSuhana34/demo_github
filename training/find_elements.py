'''EG 1'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
# footer_elements=driver.find_elements('xpath','//div[@class="footer-menu-wrapper"]//a')
# # print(footer_elements)
#
# for ele in footer_elements:
#     print(ele.text)

##############################################################################################

'''EG 2'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
#
# categories= driver.find_elements('xpath','//div[@class="block block-category-navigation"]//a')
# ##print(categories)
#
# for ele in categories:
#     print(ele.text)


######################################################################################################

'''EG 3'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get(r"C:\Users\faiza\PycharmProjects\Selenium_training\files\demo.html")
# time.sleep(2)
#
# all_textboxes=driver.find_elements('xpath','//input[@name="fname"]')
#
# data_list=['breaking bad','sherlock holmes','stranger things','family man','squid game','my demon','freelancer','bloodhounds','suits']
# for textbox ,data in zip(all_textboxes,data_list):
#     textbox.send_keys(data)

###################################################################################################################

'''EG 4'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get(r"C:\Users\faiza\PycharmProjects\Selenium_training\files\demo.html")
# time.sleep(2)
#
# all_checkboxes=driver.find_elements('xpath','//input[@name="download"]')
#
# for checkbox in all_checkboxes:
#     checkbox.click()

#################################################################################################

'''EG 5'''

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://www.python.org/")
# time.sleep(2)
#
# all_links=driver.find_elements("tag name","a")
#
# for link in all_links:
#     print(link.get_attribute('href'))















































