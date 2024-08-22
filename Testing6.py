import argparse
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

parser = argparse.ArgumentParser()
parser.add_argument('--browserName', help="enter the browser", default="chrome")

global browserName
# Parse the arguments
args = parser.parse_args()
print(args)
browserName = args.browserName

if browserName == 'chrome':
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
elif browserName == 'firefox':
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == 'edge':
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
else:
    print('Enter correct browser here')
    # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    time.sleep(5)
# driver.maximize_window()
# def close(context):
#     context.driver.close()
