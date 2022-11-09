import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By

from Utilities.configreader import ConfigReader
from features.pageobject.Base import BaseSettingsPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Search(BaseSettingsPage):
    def __init__(self,driver):
        super().__init__(driver)
    def OpenPage(self,url):
        self.driver.get(url)
        self.DynamicImplicitWait(40)
    def clickclose(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("close_XPATH")
    def Click_loginhomepage(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("LOGINHOMEPAHEBUTTON_XPATH")
    def Enter_Username(self,username):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("USERNAME_XPATH",username)
    def Enter_password(self,password):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("PASSWORD_XPATH", password)
    def Click_login(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("LOGINBUTTON_XPATH")
    # def text_Searchbar(self,searchTEXT):
    #     #WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")))
    #     self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input").click()

        # self.DynamicImplicitWait(40)
        # #self.TypeEditBox("SEARCHBAR_XPATH", searchTEXT)
        # self.driver.find_element(By.NAME,"q").send_keys(searchTEXT)

    def text_Searchbar(self, searchTEXT):
        WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")))
        self.DynamicImplicitWait(40)
        self.TypeEditBox("SEARCHBAR_XPATH", searchTEXT)


    def Click_SEARCHBUTTON(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("SEARCHBUTTON_XPATH")

    def Click_PRODUCT(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("PRODUCT_XPATH")

        self.DynamicImplicitWait(40)
        self.ClickButton("PRODUCT_XPATH")
        self.windowsIDs = self.driver.window_handles
        self.parentwindowid = self.windowsIDs[0]
        childwindowid = self.windowsIDs[1]
        self.driver.switch_to.window(childwindowid)


    def Click_ADDTOCART(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("ADDTOCART_XPATH")














