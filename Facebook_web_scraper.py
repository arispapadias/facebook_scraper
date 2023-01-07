import requests
import random

from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from secrets import username, password

class FaceBookBot():

    #NEED TO HAVE A CHROME WEBDRIVER
    def __init__(self):
        options = webdriver.Chrome('C:\webdrivers\chromedriver.exe')
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-notifications')
        self.driver = webdriver.Chrome(options=options)

    def login(self,username, password):
        self.driver.get("https://www.facebook.com/login")

        sleep(2)

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        password_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login_btn.click()

        sleep(2)



    def log_in_basic(self):
        POST_LOGIN_URL = 'https://mbasic.facebook.com/login'

        payload = {
            'email': username,
            'pass': password
        }

        with requests.Session() as session:
            post = session.post(POST_LOGIN_URL, data=payload)

    def post_likes(self):
        
        POST_LOGIN_URL = 'https://mbasic.facebook.com/login'

        
        #post_ID = 'the-post-ID'
        #limit = 200
        REQUEST_URL = f'{Your mbasic post link }'

        payload = {
            'email': username,
            'pass': password
        }

        with requests.Session() as session:
            post = session.post(POST_LOGIN_URL, data=payload)
            r = session.get(REQUEST_URL)
        soup = BeautifulSoup(r.content, "html.parser")
        names = soup.find_all('h3', class_='be')
        people_who_liked = []
        for name in names:
            people_who_liked.append(name.text)

        return people_who_liked
    ########################## IN PROGRESS ##################
    # def post_shares(self):
       
    #     POST_LOGIN_URL = 'https://mbasic.facebook.com/login'

    #     #post_ID = 'the-post-ID'
       
    #     REQUEST_URL = f'{Your Post-Share mbasic link}'

    #     payload = {
    #         'email': username,
    #         'pass': password
    #     }

    #     with requests.Session() as session:
    #         post = session.post(POST_LOGIN_URL, data=payload)
    #         r = session.get(REQUEST_URL)
    #     soup = BeautifulSoup(r.content, "html.parser")
    #     names = soup.find_all('span')
    #     people_who_shared = []
    #     for name in names:
    #         people_who_shared.append(name.text)

    #     return people_who_shared

    
    def page_likes(self):
        self.login(username, password)

        #page_name = "your-page-name"
       
        REQUEST_URL = f'{Page likes link from a token}'

        self.driver.get(REQUEST_URL)

        sleep(6)

        for i in range(1,120):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(3)
   
        page = self.driver.page_source
        soup = BeautifulSoup(page, "html.parser")
        names = soup.find_all('a', class_='_3cb8')
        people_who_follow = []
        for name in names:
            people_who_follow.append(name.text)

        return people_who_follow

       
       
    def select_winner(self,list_A,list_B):
        eligible_to_win = []
        for name in list_A:
            if name in list_B :
                eligible_to_win.append(name)
        return eligible_to_win

bot = FaceBookBot()
people_who_follow = bot.page_likes()
people_who_liked = bot.post_likes()
#people_who_shared = bot.post_shares()



eligible = bot.select_winner(people_who_liked,people_who_follow)


winner = random.choice(eligible)
print("O/H νικητής/τρια του διαγωνισμού είναι: " +winner)

