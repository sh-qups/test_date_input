import sys, os
import pyautogui
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import time
from pages.base_page import BasePage
from utils.locators import NoteWriterPageLocator

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC

class NoteWriterPage(BasePage):

    def __init__(self, driver):
        self.locator = NoteWriterPageLocator
        super(NoteWriterPage, self).__init__(driver)



    def test_tooltip(self):
        time.sleep(1)
        # ActionChains(self.driver).move_to_element(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(( By.XPATH, "//button[@class='button']")))).perform()
        # pyautogui.alert('This is an alert box.')
        element1 = self.find_element(*self.locator.mybutton)

        action= ActionChains(self.driver)
        action.move_to_element_with_offset(element1, 5, 5)
        action.perform()
        location = element1.location
        size = element1.size
        print(location, size, sep='\n')
        pyautogui.moveTo(location['x'], location['y'])
        action.move_to_element_with_offset(element1, 5, 5)
        action.perform()
        time.sleep(6)
        # pyautogui.moveTo(388, 252)
        # hover = ActionChains(self.driver).move_to_element(element1)
        # pyautogui.move(10, 10)
        # time.sleep(2)
        # pyautogui.move(10, 10)
        # time.sleep(2)
        # pyautogui.move(10, 10)
        # time.sleep(2)
        # pyautogui.move(10, 10)
        # time.sleep(2)
        # pyautogui.move(10, 10)
        # hover.perform()
        # location = element1.location
        # size = element1.size
        # print(location, size, sep='\n')
        # pyautogui.moveTo(location['x'], location['y'])
        # pyautogui.moveTo(388, 252)
        # hover = ActionChains(self.driver).move_to_element(element1)
        # hover.perform()
        # time.sleep(6)
        # hover = ActionChains(self.driver).move_to_element(element1)
        # hover.perform()
        # element2 = self.find_element(*self.locator.myparagraph)
        # hover = ActionChains(self.driver).move_to_element(element2)
        # hover.perform()
        # element3 = self.find_element(*self.locator.myicon)
        # hover = ActionChains(self.driver).move_to_element(element3)
        # hover.perform()


        # element1 = self.find_element(*self.locator.mybutton)
        # ActionChains(self.driver).move_to_element(element1).move_by_offset(2, 2).perform()
        #
        # time.sleep(2)
        # # tool_tip_elm = WebDriverWait(self.driver, 10).until( expected_conditions.visibility_of_element_located(((By.XPATH, "//button[@class='button']"))))
        # # ActionChains(self.driver).move_to_element(element1).build().perform()
        # # abc = ActionChains(self.driver).move_to_element(element1)
        # element2 = self.find_element(*self.locator.myparagraph)
        # ActionChains(self.driver).move_to_element(element2).move_by_offset(1, 2).perform()
        # time.sleep(2)
        # abc = ActionChains(self.driver)
        # abc.move_to_element(element1)
        # abc.perform()
        # abc.move_by_offset(2, 2)
        # abc.perform()
        # abc.move_by_offset(2, 2)
        # abc.perform()
        #
        # # element1.click()
        # time.sleep(3)
        # element3 = self.find_element(*self.locator.myicon)
        # ActionChains(self.driver).move_to_element(element3).move_by_offset(1, 1).perform()
        # time.sleep(3)
        # # element3.click()
        #
        #
        #
        #
        # if element1:
        #
        #     print("element found")
        #     print(element1.get_attribute("title"))
        # if element3:
        #     print("element found")
        #     print(element3.get_attribute("title"))

        time.sleep(0)




        # element2 = self.find_element(*self.locator.myparagraph)
        # element3 = self.find_element(*self.locator.myicon)
        # if element1:
        #     print("element found")
        #     print(element1.get_attribute("title"))
        # # self.hover(element1)
        # self.hover(*self.locator.mybutton)
        # time.sleep(5)
        #
        # if element2:
        #     print("element found")
        #     print(element2.get_attribute("title"))
        # # self.hover(element1)
        # self.hover(*self.locator.myparagraph)
        # time.sleep(5)



        # element = self.find_element(*self.locator.myicon)
        # print(element)
        # if element is True:
        #     print("element found")
        # # element.click()
        # # self.hover(element)
        # time.sleep(10)






    # def test_date(self):
    #     #########
    #     # time.sleep(5)
    #     # js = 'alert("Hello World")'
    #     # self.driver.execute_script(js)
    #
    #     ##################
    #     time.sleep(3)
    #     element = self.find_element(*self.locator.dateinputId)
    #     # element.send_keys('2015-05-25')   # not correct  wrong format
    #     # element.send_keys('05-25-2015')   # correct
    #     # element.send_keys('5-25-2015')    # correct
    #     # element.send_keys('5/25/2015')    # correct
    #     # element.send_keys("02022018")     # correct
    #
    #     ###############################
    #
    #     # element.send_keys('/26/')  # correct  single date
    #     # time.sleep(2)
    #     # element.send_keys('/25/')  # correct
    #     # time.sleep(2)
    #     # element.send_keys('/21/')  # correct
    #     # time.sleep(2)
    #     # element.send_keys('/31/')  # correct
    #     # time.sleep(2)
    #
    #     ###################
    #     # element.click()
    #     # element.send_keys('15')  #
    #
    #     # self.driver.execute_script("arguments[0].min = new Date('2010-01-01')", element)
    #
    #     self.driver.execute_script("arguments[0].setAttribute('min', new Date('2015-12-12').toISOString().split('T')[0] )", element)
    #     self.driver.execute_script("arguments[0].setAttribute('max', new Date('2025-12-12').toISOString().split('T')[0] )", element)
    #     # self.driver.execute_script("arguments[0].setAttribute('min', new Date('2015-12-12') )", element)
    #     # self.driver.execute_script("arguments[0].setAttribute('max', new Date('2025-12-12') )", element)
    #     element.send_keys('5/25/2021')
    #     time.sleep(6)
    #     self.driver.execute_script("arguments[0].max = new Date('2030-12-12')", element)
    #     time.sleep(6)
    #     element.clear()
    #     time.sleep(4)
    #     element.send_keys('5/26/2021')
    #
    #
    #
    #     ###################
    #
    #     # self.driver.execute_script("arguments[0].disabled = true ",element)
    #     # time.sleep(3)
    #     # self.driver.execute_script("arguments[0].disabled = false ",element)
    #
    #
    #     #########################
    #     # self.driver.execute_script("arguments[0].type = 'text'",element)
    #     # self.driver.execute_script("arguments[0].value = '10/18/2015'",element)         # correct
    #     # self.driver.execute_script("arguments[0].value = new Date('2015-03-25')",element)         # correct
    #     # self.driver.execute_script("arguments[0].value = new Date('2021-03-25').toISOString().split('T')[0]",element)         # correct
    #     # self.driver.execute_script("arguments[0].type = 'date'",element)
    #
    #
    #     # self.driver.execute_script("arguments[0].type = 'text'",element)
    #     # self.driver.execute_script("arguments[0].value = '10/18/2015'",element)         # correct
    #     # self.driver.execute_script("arguments[0].value = '05-18-2015'",element)         # correct
    #     # self.driver.execute_script('arguments[0].value = 02022018',element)
    #     # self.driver.execute_script("document.getElementById('mydate').value = '10-18-2019';")
    #     # self.driver.execute_script("arguments[0].value = '10-18-2015';", element)
    #
    #     ################################  need to be tested
    #     # element.click()
    #     # element.send_keys('-15-')      #
    #     # element.send_keys('05')
    #
    #
    #     time.sleep(3)
    #     if element:
    #          print("Element found")
    #          print(element.get_attribute('value'))
    #          print(element.get_attribute('type'))
    #     time.sleep(5)
    #
    #
    #     # self.find_element(*self.locator.dateinputXpath).click()
