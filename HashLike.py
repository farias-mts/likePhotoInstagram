import chromedriver_autoinstaller
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time

class Instagram():
    def __init__(self):
        chromedriver_autoinstaller.install()
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get('http://www.instagram.com')

    def login(self, username, password):
        time.sleep(5)
        self.browser.find_element_by_name('username').send_keys(username)
        self.browser.find_element_by_name('password').send_keys(password)
        self.browser.find_element_by_name('password').send_keys(Keys.ENTER)
    
    def HashLike(self, list_hashtag, Photos):
        time.sleep(5)
        for hashtag in list_hashtag:
            print(hashtag)
            link_hashtag = 'https://www.instagram.com/explore/tags/'+hashtag
            self.browser.get(link_hashtag)
            time.sleep(2)
            numPhotos = int((int(Photos)-39)/20)
            link_posts = []
            count=0
            if numPhotos > 1:
                for number in range(numPhotos):
                    for link in self.browser.find_elements_by_class_name('v1Nh3'):
                        post = link.find_element_by_tag_name('a').get_attribute('href')
                        if post not in link_posts:
                            link_posts.append(post)
                            count+=1
                    self.browser.execute_script('''
                        window.scrollTo(0, document.body.scrollHeight);
                    ''')
                    time.sleep(1)
                for post in link_posts:
                    try:
                        self.browser.get(post)
                        time.sleep(8)
                        btn_like = self.browser.find_element_by_xpath('//span[@class="fr66n"]')
                        #print(btn_like.find_element_by_tag_name('svg').get_attribute('aria-label'))
                        if btn_like.find_element_by_tag_name('svg').get_attribute('aria-label') == 'Curtir':
                            btn_like.find_element_by_tag_name('button').send_keys(Keys.ENTER)
                    except:
                        pass
        
    def likeFeed(self):
        time.sleep(5)
        self.browser.get('https://www.instagram.com/')
        time.sleep(5)
        self.browser.send_keys(Keys.ENTER)
        condition = True
        while condition is True:
            btns_like = self.browser.find_elements_by_xpath('//span[@class="fr66n"]')
            for btn_like in btns_like:
                if btn_like.find_element_by_tag_name('svg').get_attribute('aria-label') == 'Curtir':
                    btn_like.find_element_by_tag_name('button').send_keys(Keys.ENTER)
                    time.sleep(4)
            btns_like = None
            self.browser.execute_script('''
                window.scrollTo(0, document.body.scrollHeight);
            ''') 
            time.sleep(1)
            
user_ = "your user" #your user
pass_ = "your pass" #your pass
qtd_photos = 300 #Quantidade de fotos para curtir p/ hashtag
list_hashtag = [
    'sextou',
    'sabadou',
    'bipolar'
]


teste = Instagram()
teste.login(user_, pass_)
teste.HashLike(list_hashtag, qtd_photos)
    



