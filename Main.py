from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from time import sleep

from login_info import username, password
class Tinderbot():
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
    
    def login(self):
        self.driver.get('https://tinder.com/')

        try:
            mre = self.driver.find_element_by_xpath("//button[contains(text(), 'More Options')]")
            mre.click()

            sleep(5)

            fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
            fb_btn.click()
        except:
            pass
        try:
            fb_btn2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
            fb_btn2.click()
        except:
            pass
        try:
            fb_btn3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button')
            fb_btn3.click()
        except:
            pass
        try:
            fb_btn4 = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/div[3]/button').click()
            fb_btn4.click()
        except:
            pass

        # fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        # fb_btn.click()

        # base_window = self.driver.window_handles[0]
        # self.driver.switch_to_window(self.driver.window_handles[1])

        # email_in = self.driver.find_element_by_xpath()
        # email_in.send_keys(username)

        # pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        # pw_in.send_keys(password)

        # login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        # login_btn.click()

        # self.driver.switch_to_window(base_window)

        # popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        # popup_1.click()

        # popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        # popup_2.click()

    #def like(self):
        # like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        # like_btn.click()

    #def dislike(self):
        # dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        # dislike_btn.click()

    #def auto_swipe(self):
    
        # while True:
        #     sleep(0.5)
        #     try:
        #         self.like()
        #     except Exception:
        #         try:
        #             self.close_popup()
        #         except Exception:
        #             self.close_match()

    #def close_popup(self):
        # popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        # popup_3.click()

    #def close_match(self):
        # match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        # match_popup.click()

bot = Tinderbot()
bot.login()
