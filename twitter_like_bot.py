from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

BASE_URL = "https://twitter.com"


class Twitter_Bot:
    def __init__(self, username, password):
        # set username and password
        self.username=username
        self.password=password
        self.bot=webdriver.Chrome()


    def login(self):
        # login with the credentials
        bot = self.bot
        bot.get(BASE_URL)
        time.sleep(2)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self, hashtag):
        # like tweets
        bot = self.bot
        bot.get(BASE_URL + "/search?q=" + hashtag + "&src=typd") 
        time.sleep(3)

        for i in range(1, 3):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(2)   
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]

            for link in links:
                bot.get(BASE_URL + link)
                try:
                    bot.find_elements_by_class_name('HeartAnimation').click()
                    time.sleep(1)

                except:
                    time.sleep(3)


twitter_bot = Twitter_Bot("my_email@gmail.com", "password123")
twitter_bot.login()