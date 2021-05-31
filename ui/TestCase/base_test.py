import pathlib
import sys
import os

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--start-fullscreen")
        self.driver = webdriver.Chrome(executable_path=pathlib.Path(__file__).parent / "../browser/chromedriver")
        # self.driver = webdriver.Chrome(executable_path=pathlib.Path(__file__).parent / "../browser/geckodriver")
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(3000)
        self.driver.get('http://localhost:7272/')

    def tearDown(self):
        self.driver.close()


class TestCase(object):
    pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner(verbosity=1).run(suite)
