import  pytest

# @pytest.mark.dependency()                                #independent testcase
# def test_login():
#     print("login executing")
#
# @pytest.mark.dependency(depends=["test_login"])          #dependent testcase
# def test_logout():
#     print("logout executing")

###########################################################################################

# @pytest.mark.dependency()                                #independent testcase
# def test_login():
#     pt("login executing")
#
# @pytest.mark.dependency(depends=["test_login"])          #dependent testcase
# def test_logout():
#     print("logout executing")

###############################################################################################

# @pytest.mark.dependency()                                #independent testcase
# def test_login():
#     print("login executing")
#
# @pytest.mark.dependency()                                #independent testcase
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.dependency(depends=["test_login","test_reg"])          #dependent testcase
# def test_logout():
#     print("logout executing")

####################################################################################################

# @pytest.mark.dependency()                                #independent testcase
# def test_login():
#     print("login executing")
#
# @pytest.mark.dependency()                                #independent testcase
# def test_reg():
#     p("reg executing")
#
# @pytest.mark.dependency(depends=["test_login","test_reg"])          #dependent testcase
# def test_logout():
#     print("logout executing")

######################################################################################################

# class TestSample:
#
#     @pytest.mark.dependency()                                #independent testcase
#     def test_login(self):
#         print("login executing")
#
#     @pytest.mark.dependency(depends=['test_login'])          #dependent testcase
#     def test_logout(self):
#         print("logout executing")

######################################################################################################

# class TestSample:
#
#     @pytest.mark.dependency()                                #independent testcase
#     def test_login(self):
#         print("login executing")
#
#     @pytest.mark.dependency(depends=['TestSample::test_login'])          #dependent testcase
#     def test_logout(self):
#         print("logout executing")

#########################################################################################################

# class TestSample:
#
#     @pytest.mark.dependency()                                #independent testcase
#     def test_login(self):
#         pr("login executing")
#
#     @pytest.mark.dependency(depends=['TestSample::test_login'])          #dependent testcase
#     def test_logout(self):
#         print("logout executing")

#####################################################################################################

# class TestSample:
#
#     @pytest.mark.dependency()                                #independent testcase
#     def test_login(self):
#         print("login executing")
#
#     @pytest.mark.dependency()                                #independent testcase
#     def test_reg(self):
#         print("reg executing")
#
#     @pytest.mark.dependency(depends=['TestSample::test_login','TestSample::test_reg'])          #dependent testcase
#     def test_logout(self):
#         print("logout executing")

#####################################################################################################

# import time
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# wait_obj = WebDriverWait(driver, 5)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# @pytest.mark.dependency()               ## Independent
# def test_login():
#     driver.find_element('id', 'user-name').send_keys('standard_user')
#     time.sleep(1)
#     driver.find_element('id', 'password').send_keys('secret_sauce')
#     time.sleep(1)
#     driver.find_element('id', 'login-button').click()
#     time.sleep(3)
#     wait_obj.until(EC.visibility_of_element_located(('xpath', '//span[text()="Products"]')))
#
#
# @pytest.mark.dependency(depends=['test_login'])
# def test_logout():
#     driver.find_element('id', 'react-burger-menu-btn').click()
#     time.sleep(2)
#     driver.find_element('id', 'logout_sidebar_link').click()





























