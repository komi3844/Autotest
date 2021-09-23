import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Tensorru(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe")
        self.driver.maximize_window()

    def test_01(self):
        driver = self.driver
        driver.get("https://yandex.ru")
        driver.find_element_by_partial_link_text('Картинки').click()
        time.sleep(7)
        tabs = driver.window_handles  # список
        driver.switch_to.window(tabs[1])
        driver.find_element_by_class_name('PopularRequestList-SearchText').click()
        time.sleep(4)
        img1 = driver.find_elements_by_class_name('serp-item__link')  # список элементов
        img_link = img1[0].get_attribute('href')
        driver.get(img_link)
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[13]/div[1]/div/div/div[3]/div/div[1]/div[1]/div[4]/i").click()
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[13]/div[1]/div/div/div[3]/div/div[1]/div[1]/div[1]/i").click()
        time.sleep(4)


if __name__ == "__main__":
    unittest.main()
