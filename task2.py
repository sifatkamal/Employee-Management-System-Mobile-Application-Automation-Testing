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

    wait = WebDriverWait(driver, 15)

    wait.until(EC.presence_of_element_located(

        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter Email")')

    ))

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter Email")').send_keys('azmin@excelbd.com')

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter Password")').send_keys('D!m77(2SJ,5j')

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login")').click()

    wait.until(EC.presence_of_element_located(

        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(4)')

    ))

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(4)').click()

    driver.implicitly_wait(5)

    driver.find_element(AppiumBy.XPATH, '(//android.view.ViewGroup)[38]').click()



    wait.until(EC.presence_of_element_located(

        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Application")')

    ))   

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Application")').click()




    wait.until(EC.presence_of_element_located(

        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(14)')

    ))   


    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(14)').click()

    driver.implicitly_wait(4)
    
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Special Leave")').click()

    # # Leave cat

    wait.until(EC.presence_of_element_located(

        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(17)')

    ))

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(17)').click()

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Medical")').click()

    # # From

    wait.until(EC.presence_of_element_located(

        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("From Date*")')

    ))

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("From Date*")').click()





    wait.until(EC.presence_of_element_located(

        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("14")')

    ))
    
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("14")').click()

    driver.implicitly_wait(4)

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/button1")")').click()

    # # ========================================================================= 

    # # To

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("To Date*")').click()


    # # Go next month

    driver.implicitly_wait(2)

    # driver.find_element(AppiumBy.ID, 'android:id/next').click()

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/button1")")').click()

    # # Date

    driver.find_element(AppiumBy.ID, 'new UiSelector().text("18")').click()

    driver.implicitly_wait(4)

    # driver.find_element(AppiumBy.ID, 'android:id/button1")').click() 

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/button1")")').click()

    # # Apply Button

    driver.find_element(AppiumBy.ID, 'new UiSelector().text("Apply")').click()


    


except:

    print("FAILED")

    # driver.quit()
