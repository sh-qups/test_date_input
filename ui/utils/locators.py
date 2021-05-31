from selenium.webdriver.common.by import By

class NoteWriterPageLocator(object):

    dateinputId =(By.ID, "mydate")
    myanchor =(By.ID, "anchor")
    dateinputXpath =(By.XPATH, "//button[@lass='date_container']")
    myicon =(By.XPATH, "//i[@class='sub-status-icon nosync ng-star-inserted']")
    mybutton =(By.XPATH, "//button[@class='button']")
    myparagraph =(By.XPATH, "//p[@class='paragraph']")
