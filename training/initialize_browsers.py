
'''                Intializing Edge browser               '''


#from selenium import webdriver
#e_driver=webdriver.Edge()
## The edge browser automatically closes

#to prevent the browser from automatically closing

#from selenium import webdriver
#opts=webdriver.EdgeOptions()
#opts.add_experimental_option("detach",True)
#e_driver=webdriver.Edge(opts)

#####################################################################################

'''                    Intializing Chrome browser             '''


#from selenium import webdriver
#c_driver=webdriver.Chrome()
##The chrome browser automatically closes

#to prevent the browser from automatically closing

#from selenium import webdriver
#opts=webdriver.ChromeOptions()
#opts.add_experimental_option("detach",True)
#c_driver=webdriver.Chrome(opts)


#####################################################################################

'''                   Initializing Firefox Browser                 '''

#from selenium import webdriver
#f_driver = webdriver.Firefox()

##firefox will not automatically close
##So no need to consider FirefoxOptions and add_experimental_option


#######################################################################################
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
driver=Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
sleep(5)
driver.find_element(By.ID,"firstName").send_keys("FATHIMA")
sleep(5)