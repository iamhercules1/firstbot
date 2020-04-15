from selenium import webdriver
from time import sleep

from secrets import username, password

class Tinderbot ():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get(https://tinder.com/)

        sleep(2)

        fb_btn = self.driver.find_element(//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button)
