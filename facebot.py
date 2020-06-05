from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
import time

class pic_pull():
    def __init__(self):
        self.driver = webdriver.Chrome()
        action = ActionChains(self.driver)

    def downloadit(self):
        pic = self.driver.find_element_by_xpath('//*[@id="photos_snowlift"]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/img')
        action = ActionChains(self.driver)
        action.context_click(pic).perform()
        #window_after = self.driver.window_handles[1]
        pyautogui.typewrite(['s'])
        pyautogui.typewrite(['enter'])
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(1)
        pyautogui.typewrite(['enter'])

    def getall(self):
        for x in range(1000):
            self.downloadit()
            time.sleep(1)
            pyautogui.press(['left'])
            time.sleep(2)
