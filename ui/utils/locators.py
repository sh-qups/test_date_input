from selenium.webdriver.common.by import By

class NoteWriterPageLocator(object):

    dateinputId =(By.ID, "mydate")
    dateinputXpath =(By.XPATH, "//button[@lass='date_container']")