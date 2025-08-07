from appium import webdriver
from appium.options.android import UiAutomator2Options
from os import path
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

CUR_DIR = path.dirname(path.abspath(__file__))


APP = r'F:\5. Activities\Apk file\mobile-app.apk'


APPIUM = 'http://localhost:4723'
CAPS = {
    'platformName': 'Android',
    'deviceName': 'Android Emulator',
    'automationName': 'UIAutomator2',
    'app': APP,
    "autoGrantPermissions": True
}

options = UiAutomator2Options().load_capabilities(CAPS)

driver = webdriver.Remote(
    command_executor=APPIUM,
    options=options
)

try:

    wait = WebDriverWait(driver, 10)

    wait.until(EC.presence_of_element_located(

        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter Email")')

    ))

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter Email")').send_keys('azmin@excelbd.com')

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter Password")').send_keys('D!m77(2SJ,5j')

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login")').click()

    wait.until(EC.presence_of_element_located(

        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(2)')

    ))

    myAttendance = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(2)')

    myAttendance.click()

except:

    driver.quit()
