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

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(2)').click()



    wait.until(EC.presence_of_element_located(

        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("From")')

    ))

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("From")').click()

    

    wait.until(EC.presence_of_element_located(

        (AppiumBy.ID, 'android:id/prev')

    ))

    driver.find_element(AppiumBy.ID, 'android:id/prev').click()

    driver.find_element(AppiumBy.ID, 'android:id/prev').click()

    wait.until(EC.presence_of_element_located(

        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("6")')

    ))
    
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("6")').click()

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/button1")').click()

    wait.until(EC.presence_of_element_located(

        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("To")')

    ))

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("To")').click()

    wait.until(EC.presence_of_element_located(

        (AppiumBy.ID, 'android:id/next')

    ))   

    driver.find_element(AppiumBy.ID, 'android:id/prev').click()

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("6")').click()

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/button1")').click()

    wait.until(EC.presence_of_element_located(

        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("All")')

    ))

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("All")').click()

    wait.until(EC.presence_of_element_located(

        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("On Leave")')

    ))



    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("On Leave")').click()

    time.sleep(3)

    rows = driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").descriptionContains(",")')

    data = []

    for i in rows:
        
        data.append(i.get_attribute("content-desc"))

    assert data!=[]

    timeStamp = int(time.time())

    filename = f"screenshots/result_{timeStamp}.png"

    driver.get_screenshot_as_file(filename)

    time.sleep(3)

    driver.close_app()
    

except:


    driver.quit()
