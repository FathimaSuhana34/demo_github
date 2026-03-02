# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://www.myntra.com/")
# time.sleep(2)
# driver.find_element('xpath','//input[@class="desktop-searchBar"]').send_keys("adidas shoes")
# time.sleep(1)
# driver.find_element('xpath','//a[@class="desktop-submit"]').click()
# time.sleep(2)
#
# shoe_names=driver.find_elements('xpath','//h4[@class="product-product"]')
# shoe_prices=driver.find_elements('xpath','//span[@class="product-discountedPrice"]')
#
#
# for name,price in zip(shoe_names,shoe_prices):
#     print(f"{name.text}={price.text}")

###################################################################################################

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
#
# driver.get("https://www.myntra.com/")
# time.sleep(2)
# driver.find_element('xpath','//input[@class="desktop-searchBar"]').send_keys("adidas shoes")
# time.sleep(2)
# driver.find_element('xpath','//a[@class="desktop-submit"]').click()
# time.sleep(2)
# driver.find_element('xpath','//div[@class="colour-more"]').click()
#
# colours=driver.find_elements('xpath','(//div[@class="vertical-filters-filters"])[2]//li')
#
# for colour in colours:
#     print(colour.text)

#####################################################################################################


# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.get("https://in.bookmyshow.com/")
# time.sleep(5)
# driver.find_element('xpath','//input[@placeholder="Search for your city"]').send_keys("kayamkulam")
# time.sleep(3)
# driver.find_element('xpath','//div[@data-result-item="true"]').click()
# time.sleep(3)
# recommended_movies=driver.find_elements('xpath','(//div[@class="sc-133848s-3 sc-133848s-5 bbHlLd bTYjFI"])[1]')
#
# for movies in recommended_movies:
#     print(movies.text)

######################################################################################################################

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.get('https://www.zomato.com/thrissur/restaurants')
# time.sleep(4)
# driver.find_element('xpath','//input[@placeholder="Search for restaurant, cuisine or a dish"]').send_keys("domino's pizza")
# time.sleep(3)
# driver.find_element('xpath','''//p[text()="Domino's Pizza"]''').click()
#
# driver.find_element('xpath','//div[@class="sc-hCbubC jCiGyG"]').click()
# time.sleep(2)

































