from selenium.webdriver.chrome.options import Options

FeelingLucky = "(//*[@class='RNmpXc'])[2]"
About = 'xpath://*[@id="about-link"]'
burrning = "xpath://*[text()='Burning Man festival']"
# URL = "http://192.168.0.33:8080/login"
URL = "https://www.google.com/"


class GenericMethod:

    def Options12(self):
        options1 = Options()
        # prefs = {"credentials_enable_service": False,
        #          "profile.password_manager_enabled": False}
        options1.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options1.add_experimental_option("prefs", prefs)
        # options1.add_experimental_option("detach", True)


gen = GenericMethod()
