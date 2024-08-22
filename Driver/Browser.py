import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# parser = argparse.ArgumentParser()
# parser.add_argument('browserName', help="enter the browser")

global browserName
browserName = "chrome"

# Parse the arguments
# args = parser.parse_args()
# print(args)
# browserName = args.browserName


if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "edge":
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    print('please pass the correct browser name :' + browserName)
time.sleep(3)
