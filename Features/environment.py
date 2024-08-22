# from Testing6 import *
import smtplib
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver import EdgeOptions
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdrivermanager import EdgeChromiumDriverManager, GeckoDriverManager

from Utilities.GenericMethod import myLogger

options1 = Options()
prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False}
options1.add_experimental_option("excludeSwitches", ["enable-automation"])
options1.add_experimental_option("prefs", prefs)
options1.add_experimental_option("detach", True)
# options1.add_argument("--headless")
# options1.add_argument("--window-size=1920,1080")

options2 = EdgeOptions()
prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False}
options2.add_experimental_option("excludeSwitches", ["enable-automation"])
options2.add_experimental_option("prefs", prefs)
options2.add_experimental_option("detach", True)


def before_all(context):
    # *****************************************************************************************************#
    # global browserName
    # browserName = input("Enter the Browser")
    #
    # if browserName == 'chrome':
    #     driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options1)
    # elif browserName == 'firefox':
    #     driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    # elif browserName == 'edge':
    #     driver = webdriver.Edge(EdgeChromiumDriverManager().install(), options=options2)
    # else:
    #     driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options1)
    #     time.sleep(5)
    # # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options1)
    driver = webdriver.Chrome(executable_path='D:\Bestinet\Driver\chromedriver.exe', options=options1)
    context.driver = driver
    myLogger.info("****** Driver Initialized ******")
    context.driver.maximize_window()
    # c = f'behave'


def before_scenario(context, scenario):
    # height = GetSystemMetrics(1)
    # width = GetSystemMetrics(0)
    # time_stamp = datetime.datetime.now().strftime(
    #     '%Y-%m-%d %H-%M-%S')
    # file_name = f'{time_stamp}.mp4'
    # fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    # final_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))
    # while True:
    #     img = ImageGrab.grab(bbox=(0, 0, width, height))
    #     img_ny = ny.array(img)
    #     img_final = cv2.cvtColor(img_ny, cv2.COLOR_BGR2RGB)
    #     final_video.write(img_final)

    time.sleep(1)


def after_step(context, step):
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
        context.driver.get_screenshot_as_file(".\Fail-ScreenShots\Capture.png")
        fromaddr = "noreply.phoenix@esspl.com"
        toaddr = ["debadatta@esspl.com", "swadhin@esspl.com"]
        # toaddr = "debadatta@esspl.com"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        # Multiple email send
        msg['To'] = ",".join(toaddr)
        # Single email send
        # msg['To'] = toaddr

        msg['Subject'] = "Error meassage"
        body = """\
                Subject: Error Message

                Dear Team,

                     Kindly find the attached screenshot for the Error.

                Thanks & Regards,
                Debadatta Pattanaik
                Senior Tester."""
        msg.attach(MIMEText(body, 'plain'))
        filename = "Capture1.png"
        attachment = open(".\Fail-ScreenShots\Capture.png", "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, "E$$pl@2022!#21")
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()

# def after_all(context):
#     # context.driver.get_screenshot_as_file(".\Fail-ScreenShots\Failed-Screenshot" + c + ".png")
#     allure.attach(context.driver.get_screenshot_as_png(), name="w", attachment_type=AttachmentType.PNG)
#     # context.driver.close()
