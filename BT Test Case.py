from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
import time
class test_login(TestCase):
    def test_landing_page(self):
        options = Options()
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
        # Launch of the application URL(https://www.bt.com/)
        driver.get('https://www.bt.com/')
        driver.implicitly_wait(20)
        frame = driver.find_element(By.CLASS_NAME, 'truste_popframe')
        driver.switch_to.frame(frame)
        # Close accept Cookie pop-up if it appears
        accept = driver.find_element(By.LINK_TEXT, 'Accept all cookies')
        accept.click()
        # Hover to Mobile menu
        driver.switch_to.default_content()
        ele = driver.find_element(By.XPATH, '(//span[text()="Mobile"])[1]')
        act = ActionChains(driver)
        act.move_to_element(ele).perform()
        time.sleep(20)
        # From mobile menu, select Mobile phones
        ele1 = driver.find_element(By.LINK_TEXT, 'Mobile phones')

        act = ActionChains(driver)
        act.move_to_element(ele1).click().perform()

        time.sleep(20)

        # Verify the numbers of banners present below “See Handset details” should not be less than 3

        # Scroll down and click View SIM only deals
        scrolDown = 'window.scroll(1500,2000)'
        driver.execute_script(scrolDown)
        simOnlyOption = driver.find_element(By.LINK_TEXT, 'View SIM only deals')
        simOnlyOption.click()

        # Validate the title for new page.
        act_title_of_window = driver.title
        print(act_title_of_window)
        exp_title_of_window='SIM Only Deals | Compare SIMO Plans & Contracts | BT Mobile'
        assert act_title_of_window==exp_title_of_window,'Actual is not expected'

        driver.quit()



