from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pyperclip

driver = webdriver.Chrome(r'C:/Users/Kim Minhyung/Desktop/selenium/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(3)

# naver 자동 로그인하기
driver.get('https://nid.naver.com/nidlogin.login')
id = 'dzf1224'
pw = '!minhk4!'
pyperclip.copy(id)
driver.find_element_by_name('id').send_keys(Keys.CONTROL + 'v')
pyperclip.copy(pw)
driver.find_element_by_name('pw').send_keys(Keys.CONTROL + 'v')
driver.find_element_by_id('log.login').click()

driver.get('https://order.pay.naver.com/home')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('div.goods_item > div.goods_info > a.goods > p.name')

for n in notices:
    str = n.text.strip()
    print(str)