

'''SINGLE SELECT LISTBOX'''

# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# driver=webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\faiza\PycharmProjects\Selenium_training\files\demo (1).html')
# time.sleep(2)
#
# listbox=driver.find_element('xpath','//select[@id="standard_cars"]')
# select_obj=Select(listbox)

##select by index
# select_obj.select_by_index(5)
# time.sleep(2)
# select_obj.select_by_index(8)

#----------------------------------------------------------------------------------

##select by value
# select_obj.select_by_value("bmw")
# time.sleep(2)
# select_obj.select_by_value("vol")

#------------------------------------------------------------------------------------

##select by visible text
# select_obj.select_by_visible_text("Ford")
# time.sleep(2)

####################################################################################################

'''MULTI SELECT LISTBOX'''


# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# driver=webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\faiza\PycharmProjects\Selenium_training\files\demo (1).html')
# time.sleep(2)
# #
# listbox=driver.find_element('xpath','//select[@id="multiple_cars"]')
# select_obj=Select(listbox)

#select by index
# select_obj.select_by_index(1)
# time.sleep(1)
# select_obj.select_by_index(2)
# time.sleep(1)
# select_obj.select_by_index(3)
# time.sleep(1)
# select_obj.select_by_index(4)
# time.sleep(1)
# select_obj.select_by_index(5)
# time.sleep(1)
# select_obj.select_by_index(6)
# time.sleep(1)
# select_obj.select_by_index(7)
# time.sleep(1)
# select_obj.select_by_index(8)
# time.sleep(1)
# select_obj.select_by_index(9)
# time.sleep(1)
# select_obj.select_by_index(10)
# time.sleep(1)
# select_obj.select_by_index(11)
# time.sleep(1)

# ##deselect by index
# select_obj.deselect_by_index(5)
# time.sleep(2)
# select_obj.deselect_by_index(8)
# time.sleep(2)
#----------------------------------------------------------------------------------

##select by value
# select_obj.select_by_value("aud")
# time.sleep(1)
# select_obj.select_by_value("bmw")
# time.sleep(1)
# select_obj.select_by_value("for")
# time.sleep(1)
# select_obj.select_by_value("hda")
# time.sleep(1)
# select_obj.select_by_value("jgr")
# time.sleep(1)
# select_obj.select_by_value("lr")
# time.sleep(1)
# select_obj.select_by_value("merc")
# time.sleep(1)
# select_obj.select_by_value("min")
# time.sleep(1)
# select_obj.select_by_value("nin")
# time.sleep(1)
# select_obj.select_by_value("toy")
# time.sleep(1)
# select_obj.select_by_value("vol")
# time.sleep(1)

# ##deselect by value
# select_obj.deselect_by_value("bmw")
# time.sleep(2)
# select_obj.deselect_by_value("vol")
# time.sleep(2)

#------------------------------------------------------------------------------------

##select by visible text
# select_obj.select_by_visible_text("Audi")
# time.sleep(1)
# select_obj.select_by_visible_text("BMW")
# time.sleep(1)
# select_obj.select_by_visible_text("Ford")
# time.sleep(1)
# select_obj.select_by_visible_text("Honda")
# time.sleep(1)
# select_obj.select_by_visible_text("Jaguar")
# time.sleep(1)
# select_obj.select_by_visible_text("Mercedes")
# time.sleep(1)
# select_obj.select_by_visible_text("Land Rover")
# time.sleep(1)
# select_obj.select_by_visible_text("Mini")
# time.sleep(1)
# select_obj.select_by_visible_text("Nissan")
# time.sleep(1)
# select_obj.select_by_visible_text("Toyota")
# time.sleep(1)
# select_obj.select_by_visible_text("Volvo")




# ##deselect by visible text
# select_obj.deselect_by_visible_text("Ford")
# time.sleep(2)
# select_obj.deselect_by_visible_text("Mercedes")
# time.sleep(2)

############################################################################################################


'''IS MULTIPLE'''

# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# driver=webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\faiza\PycharmProjects\Selenium_training\files\demo (1).html')
# time.sleep(2)
#
# multiselect_listbox=driver.find_element('xpath','//select[@id="multiple_cars"]')
# multiselect_obj=Select(multiselect_listbox)
# print(multiselect_obj.is_multiple)
#
# singleselect_listbox=driver.find_element('xpath','//select[@id="standard_cars"]')
# singleselect_obj=Select(singleselect_listbox)
# print(singleselect_obj.is_multiple)

################################################################################################

'''TO DESELECT ALL THE SELECTED ITEMS'''



# listbox=driver.find_element('xpath','//select[@id="multiple_cars"]')
# select_obj=Select(listbox)
#
# select_obj.select_by_index(5)
# time.sleep(1)
# select_obj.select_by_value("bmw")
# time.sleep(1)
# select_obj.select_by_visible_text("Ford")
# time.sleep(1)
#
# select_obj.deselect_all()

#######################################################################################

'''TO GET ALL THE SELECTED ITEMS'''

# listbox=driver.find_element('xpath','//select[@id="multiple_cars"]')
# select_obj=Select(listbox)
#
# select_obj.select_by_index(9)
# time.sleep(1)
# select_obj.select_by_value("bmw")
# time.sleep(1)
# select_obj.select_by_visible_text("Ford")
# time.sleep(1)
#
# selected_data=select_obj.all_selected_options
#
# for ele in selected_data:
#     print(ele.text)

##############################################################################################

'''FIRST SELECTED OPTION'''

# listbox=driver.find_element('xpath','//select[@id="multiple_cars"]')
# select_obj=Select(listbox)
#
# select_obj.select_by_index(9)
# time.sleep(1)
# select_obj.select_by_value("bmw")
# time.sleep(1)
# select_obj.select_by_visible_text("Ford")
# time.sleep(1)
#
# first_ele=select_obj.first_selected_option
# print(first_ele.text)

###################################################################################################

'''OPTIONS'''

# listbox=driver.find_element('xpath','//select[@id="multiple_cars"]')
# select_obj=Select(listbox)
#
# all_options=select_obj.options
#
# for option in all_options:
#     print(option.text)

##################################################################################################

'''EG 2'''

# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# driver=webdriver.Chrome(opts)
#
# driver.get('https://en-gb.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# day=driver.find_element('xpath','//select[@name="birthday_day"]')
# select_obj=Select(day)
#
# select_obj.select_by_value("9")
# time.sleep(2)
#
# month=driver.find_element('xpath','//select[@name="birthday_month"]')
# select_obj=Select(month)
#
# select_obj.select_by_visible_text("Sep")
# time.sleep(2)
#
# year=driver.find_element('xpath','//select[@name="birthday_year"]')
# select_obj=Select(year)
#
# select_obj.select_by_visible_text("2003")
# time.sleep(2)
