#insta bot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep, strftime
from random import randint
import pandas as pd

LOGIN = '' #Add instagram account here
INSTA_PASSWORD = '' #Add instagram password here

webdriver = webdriver.Chrome(ChromeDriverManager().install())
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys(LOGIN)
password = webdriver.find_element_by_name('password')
password.send_keys(INSTA_PASSWORD)

button_login = webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button/div')
button_login.click()
sleep(3)

notnow = webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
notnow.click()

dismiss = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
dismiss.click()

hashtag_list = ['Brazil', 'Vitoria', 'Beer'] #You can pass hashtags to interact with or Places
location_list = ['102862087801655/praia-da-costa-vila-velha-es/', '221160407/vila-velha-brazil/']


new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0

for hashtag in location_list:
    tag += 1
    webdriver.get('https://www.instagram.com/explore/locations/'+ location_list[tag] + '/')
    sleep(5)
    first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
    
    first_thumbnail.click()
    sleep(randint(1,2))    
    try:        
        for x in range(1,200):
            username = webdriver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a').text
            
            if username not in prev_user_list:
                # Don't unfollow accounts you already follow
                if webdriver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Seguir':
                    
                    webdriver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                    
                    new_followed.append(username)
                    followed += 1

                    # Liking the picture
                    button_like = webdriver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
                    print('curtido: ', likes)
                    button_like.click()
                    likes += 1
                    sleep(randint(18,25))

                # Next picture
                webdriver.find_element_by_link_text('Próximo').click()
                sleep(randint(25,29))
            else:
                webdriver.find_element_by_link_text('Próximo').click()
                sleep(randint(20,26))
    # If the hashtag ends, continue to the next
    except:
        continue

for n in range(0,len(new_followed)):
    prev_user_list.append(new_followed[n])

print('Liked {} photos.'.format(likes))
print('Commented {} photos.'.format(comments))
print('Followed {} new people.'.format(followed))