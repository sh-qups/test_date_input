import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import time
from pages.base_page import BasePage
from utils.locators import NoteWriterPageLocator
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class NoteWriterPage(BasePage):

    def __init__(self, driver):
        self.locator = NoteWriterPageLocator
        super(NoteWriterPage, self).__init__(driver)

    def test_date(self):
        #########
        # time.sleep(5)
        # js = 'alert("Hello World")'
        # self.driver.execute_script(js)

        ##################
        time.sleep(3)
        element = self.find_element(*self.locator.dateinputId)
        # element.send_keys('2015-05-25')   # not correct  wrong format
        # element.send_keys('05-25-2015')   # correct
        # element.send_keys('5-25-2015')    # correct
        # element.send_keys('5/25/2015')    # correct
        # element.send_keys("02022018")     # correct

        ###############################

        # element.send_keys('/26/')  # correct  single date
        # time.sleep(2)
        # element.send_keys('/25/')  # correct
        # time.sleep(2)
        # element.send_keys('/21/')  # correct
        # time.sleep(2)
        # element.send_keys('/31/')  # correct
        # time.sleep(2)

        ###################
        # element.click()
        # element.send_keys('15')  #

        # self.driver.execute_script("arguments[0].min = new Date('2010-01-01')", element)

        self.driver.execute_script("arguments[0].setAttribute('min', new Date('2015-12-12').toISOString().split('T')[0] )", element)
        self.driver.execute_script("arguments[0].setAttribute('max', new Date('2025-12-12').toISOString().split('T')[0] )", element)
        # self.driver.execute_script("arguments[0].setAttribute('min', new Date('2015-12-12') )", element)
        # self.driver.execute_script("arguments[0].setAttribute('max', new Date('2025-12-12') )", element)
        element.send_keys('5/25/2021')
        time.sleep(6)
        self.driver.execute_script("arguments[0].max = new Date('2030-12-12')", element)
        time.sleep(6)
        element.clear()
        time.sleep(4)
        element.send_keys('5/26/2021')



        ###################

        # self.driver.execute_script("arguments[0].disabled = true ",element)
        # time.sleep(3)
        # self.driver.execute_script("arguments[0].disabled = false ",element)


        #########################
        # self.driver.execute_script("arguments[0].type = 'text'",element)
        # self.driver.execute_script("arguments[0].value = '10/18/2015'",element)         # correct
        # self.driver.execute_script("arguments[0].value = new Date('2015-03-25')",element)         # correct
        # self.driver.execute_script("arguments[0].value = new Date('2021-03-25').toISOString().split('T')[0]",element)         # correct
        # self.driver.execute_script("arguments[0].type = 'date'",element)


        # self.driver.execute_script("arguments[0].type = 'text'",element)
        # self.driver.execute_script("arguments[0].value = '10/18/2015'",element)         # correct
        # self.driver.execute_script("arguments[0].value = '05-18-2015'",element)         # correct
        # self.driver.execute_script('arguments[0].value = 02022018',element)
        # self.driver.execute_script("document.getElementById('mydate').value = '10-18-2019';")
        # self.driver.execute_script("arguments[0].value = '10-18-2015';", element)

        ################################  need to be tested
        # element.click()
        # element.send_keys('-15-')      #
        # element.send_keys('05')


        time.sleep(3)
        if element:
             print("Element found")
             print(element.get_attribute('value'))
             print(element.get_attribute('type'))
        time.sleep(5)


        # self.find_element(*self.locator.dateinputXpath).click()
