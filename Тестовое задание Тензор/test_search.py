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
        search = driver.find_element_by_id('text')
        search.send_keys('тензор')
        time.sleep(5)

    def test_02(self):
        driver = self.driver
        driver.get("https://yandex.ru")
        search = driver.find_element_by_id('text')
        search.send_keys('тензор')
        search.send_keys(Keys.ENTER)
        time.sleep(5)
        self.content = driver.find_elements_by_link_text('tensor.ru')
        for contents in range(1, 5):
            assert "tensor" in self.content

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
