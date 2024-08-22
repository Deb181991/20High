import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# object of ChromeOptions
# op = webdriver.ChromeOptions()
# op1 = webdriver.ChromeOptions
# add option
options.add_experimental_option("excludeSwitches", ["enable-automation"])
# pass option to webdriver object
# driver = webdriver.Chrome(chrome_options=op)
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
url = "http://192.168.0.33:9080/"
driver.get(url)
time.sleep(20)
