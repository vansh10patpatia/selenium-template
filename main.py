from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.uptodate.com/contents/search")
login = driver.find_element(by=By.XPATH , value='//*[@id="appContainer"]/header/section/nav/div/ul[2]/li[2]/a')
login.click()
# AS518872
driver.find_element(by = By.ID, value="userName").send_keys("")
driver.find_element(by = By.ID, value="password").send_keys("")
driver.find_element(by = By.ID,value="btnLoginSubmit").click()
# //*[@id="calcHeader"]/a
driver.find_element(by=By.XPATH , value='//*[@id="calcHeader"]/a').click()
allCal = driver.find_element(by=By.ID,value="toc-sections")
innerHtml = allCal.get_attribute("innerHTML")
soup = BeautifulSoup(innerHtml, 'html.parser')
