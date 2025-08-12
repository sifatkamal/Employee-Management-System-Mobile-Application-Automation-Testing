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



#-------------------------------------------------------------------------------------



    wait.until(EC.presence_of_element_located(

        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter Email")')

    ))

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter Email")').send_keys('azmin@excelbd.com')

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter Password")').send_keys('D!m77(2SJ,5j')

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login")').click()


    wait.until(EC.any_of(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Check-OUT")')),
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Check-IN")'))
    ))

    driver.implicitly_wait(7)


    try:
        
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Check-OUT")')

        pass

    except:

        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Check-IN').click()

        driver.find_element(AppiumBy.ID, 'com.android.camera2:id/shutter_button').click()

        driver.find_element(AppiumBy.ID, 'com.android.camera2:id/done_button').click()

        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Check-IN")').click()

        assert driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Checked IN Successful")').text == "Checked IN Successful"

        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("OK")').click()
    






    wait.until(EC.presence_of_element_located(

        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(4)')

    ))

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(4)').click()

    driver.implicitly_wait(5)

    try:
        driver.find_element(AppiumBy.XPATH, '(//android.view.ViewGroup)[36]').click()
    except:
        driver.find_element(AppiumBy.XPATH, '(//android.view.ViewGroup)[31]').click()
    



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

    wait.until(EC.presence_of_element_located(

        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(17)')

    ))

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(17)').click()

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Medical")').click()


    wait.until(EC.presence_of_element_located(

        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("From Date*")')

    ))

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("From Date*")').click()

    driver.find_element(AppiumBy.ID, 'android:id/prev').click()

    driver.implicitly_wait(2)


    wait.until(EC.presence_of_element_located(

        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("11")')

    ))
    
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("11")').click()

    driver.implicitly_wait(4)

    driver.find_element(AppiumBy.ID, 'android:id/button1').click()




    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("To Date*")').click()



    driver.implicitly_wait(4)



    driver.find_element(AppiumBy.ID, 'android:id/prev').click()

    driver.implicitly_wait(2)


    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("13")').click()

    driver.implicitly_wait(4)

    driver.find_element(AppiumBy.ID, 'android:id/button1').click()




    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Apply")').click()

    driver.implicitly_wait(3)

    wait.until(EC.presence_of_element_located(

        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("OK")')

    ))

    timeStamp = int(time.time())

    filename = f"screenshots/confirmation_{timeStamp}.png"

    driver.get_screenshot_as_file(filename)

    driver.implicitly_wait(3)

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("OK")').click()

    driver.close_app()


    
    


except:

    print("Failed")

    driver.quit()
