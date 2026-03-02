import pytest

# @pytest.fixture()
# def greet():
#     print("Good morning")
#
# def test_login(greet):
#     print("login executing")
#
# def test_signup(greet):
#     print("signup executing")
#
# def test_logout(greet):
#     print("logout executing")

#####################################################################################################

# @pytest.fixture()
# def greet():
#     print("Good morning")
#
# def test_login(greet):
#     print("login executing")
#
# def test_signup(greet):
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")

######################################################################################################

# @pytest.fixture()
# def greet():
#     print("Good morning")                           #setup
#     yield
#     print("Good Night")                              #teardown
#
# def test_login(greet):
#     print("login executing")
#
# def test_signup(greet):
#     print("signup executing")
#
# def test_logout(greet):
#     print("logout executing")

#####################################################################################################

# @pytest.fixture(autouse=True)
# def greet():
#     print("Good morning")                           #setup
#     yield
#     print("Good Night")                              #teardown
#
# def test_login():
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")

###################################################################################################

# @pytest.fixture()
# def greet():
#     print("Good morning")                           #setup
#     yield
#     print("Good Night")                              #teardown
#
# class TestSample:
#
#     def test_login(self,greet):
#         print("login executing")
#
#     def test_signup(self,greet):
#         print("signup executing")
#
#     def test_logout(self,greet):
#         print("logout executing")

######################################################################################################

# @pytest.fixture(autouse=True)
# def greet():
#     print("Good morning")                           #setup
#     yield
#     print("Good Night")                              #teardown
#
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")

####################################################################################################

# @pytest.fixture(autouse=True,scope='class')
# def greet():
#     print("Good morning")                           #setup
#     yield
#     print("Good Night")                              #teardown
#
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")

#####################################################################################################

# @pytest.fixture(autouse=True,scope='module')
# def greet():
#     print("Good morning")                           #setup
#     yield
#     print("Good Night")                              #teardown
#
# def test_login():
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")

##################################################################################################

# @pytest.fixture(autouse=True)
# def greet():
#     print("Good morning")                           #setup
#     yield
#     print("Good Night")                              #teardown
#
# @pytest.fixture(autouse=True)
# def display():
#     print("Hi everyone")
#
# def test_login():
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")

##############################################################################################################

import time

from selenium import webdriver

@pytest.fixture(scope="class")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://demowebshop.tricentis.com/")
    time.sleep(2)
    yield driver
    driver.close()

class TestRegister:
    def test_reg(self,setup):
        setup.find_element('xpath','//a[text()="Register"]').click()
        time.sleep(1)

    def test_gender(self,setup):
        setup.find_element('id','gender-female').click()
        time.sleep(1)

    def test_fname(self,setup):
        setup.find_element('id','FirstName').send_keys('Fathima')
        time.sleep(1)

    def test_lname(self,setup):
        setup.find_element('id','LastName').send_keys('Suhana')
        time.sleep(1)

    def test_reg_email(self,setup):
        setup.find_element('id','Email').send_keys('fathima@gmail.com')
        time.sleep(1)

    def test_reg_pwd(self,setup):
        setup.find_element('id','Password').send_keys('fathima@123')
        time.sleep(1)

    def test_reg_confirm_pwd(self,setup):
        setup.find_element('id','ConfirmPassword').send_keys('fathima@123')
        time.sleep(1)


class TestLogin:
    def test_login(self,setup):
        setup.find_element('xpath','//a[text()="Log in"]').click()
        time.sleep(1)

    def test_login_email(self,setup):
        setup.find_element('id','Email').send_keys('fathima@gmail.com')
        time.sleep(1)

    def test_login_pwd(self,setup):
        setup.find_element('id','Password').send_keys('fathima@123')
        time.sleep(1)


































































































