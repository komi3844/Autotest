
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Eis(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r"C:\Users\support2\Desktop\Лыховид\py\Тестовое ЕИС мини ОЧ\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://zakupki.gov.ru/epz/main/public/home.html")

    # Реестр Закупки  44-ФЗ/223-ФЗ
    def test_01ZAK44(self):
        driver = self.driver
        driver.find_element_by_partial_link_text('Закупки').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@for="fz223"]').click()
        time.sleep(5)
        search = driver.find_element_by_id('searchString')
        search.send_keys('6440011981')
        time.sleep(2)
        search.send_keys(Keys.ENTER)
        time.sleep(5)
        driver.find_element_by_class_name('registry-entry__header-mid__number').click()
        time.sleep(5)

    def test_02ZAK223(self):
        driver = self.driver
        driver.find_element_by_partial_link_text('Закупки').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@for="fz44"]').click()
        time.sleep(5)
        search = driver.find_element_by_id('searchString')
        search.send_keys('8700000339')
        time.sleep(2)
        search.send_keys(Keys.ENTER)
        time.sleep(5)
        driver.find_element_by_class_name('registry-entry__header-mid__number').click()
        time.sleep(5)

    # Реестр контрактов 44-ФЗ/Реестр договоров 223-ФЗ
    def test_03RK44(self):
        driver = self.driver
        driver.find_element_by_partial_link_text('Контракты и договоры').click()
        time.sleep(3)
        driver.find_element_by_partial_link_text('Реестр контрактов').click()
        time.sleep(3)
        search = driver.find_element_by_id('searchString')
        search.send_keys('0274025624')
        time.sleep(2)
        search.send_keys(Keys.ENTER)
        time.sleep(4)
        driver.find_element_by_class_name("registry-entry__header-mid__number").click()
        time.sleep(5)

    def test_04RK223(self):
        driver = self.driver
        driver.find_element_by_partial_link_text('Контракты и договоры').click()
        time.sleep(3)
        driver.find_element_by_partial_link_text('Реестр договоров').click()
        time.sleep(3)
        search = driver.find_element_by_id('searchString')
        search.send_keys('7707049388')
        time.sleep(2)
        search.send_keys(Keys.ENTER)
        time.sleep(4)
        driver.find_element_by_class_name("registry-entry__header-mid__number").click()
        time.sleep(5)

    # ПЛАНИРОВАНИЕ 44-ФЗ/223-ФЗ
    def test_05PG44(self):
        driver = self.driver
        driver.find_element_by_partial_link_text('Планирование').click()
        time.sleep(3)
        driver.find_element_by_partial_link_text('Планы-графики закупок').click()
        time.sleep(3)
        search = driver.find_element_by_id('searchString')
        search.send_keys('3625001701')
        time.sleep(2)
        search.send_keys(Keys.ENTER)
        driver.find_element_by_class_name("registry-entry__header-mid__number").click()
        time.sleep(5)

    def test_06PG223(self):
        driver = self.driver
        driver.find_element_by_partial_link_text('Планирование').click()
        time.sleep(3)
        driver.find_element_by_partial_link_text('Планы-графики закупок').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@for="fz44"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@for="fz223"]').click()
        search = driver.find_element_by_id('searchString')
        search.send_keys('8709013318')
        time.sleep(2)
        search.send_keys(Keys.ENTER)
        driver.find_element_by_class_name("registry-entry__header-mid__number").click()
        time.sleep(5)

    # раздел КТРУ
    def test_07KTRU(self):
        driver = self.driver
        driver.find_element_by_partial_link_text('Каталог').click()
        time.sleep(2)
        driver.find_element_by_id('ItemPreview369').click()
        time.sleep(5)
        driver.execute_script("window.history.go(-1)")
        time.sleep(3)
        driver.find_element_by_id('ItemPreview-1').click()
        time.sleep(5)
        driver.execute_script("window.history.go(-1)")
        time.sleep(3)
        driver.find_element_by_id('ItemPreview371').click()
        time.sleep(5)
        driver.execute_script("window.history.go(-1)")
        time.sleep(3)
        driver.find_element_by_id('ItemPreview381').click()
        time.sleep(5)
        driver.execute_script("window.history.go(-1)")
        time.sleep(3)
        driver.find_element_by_id('ItemPreview370').click()
        time.sleep(5)
        driver.execute_script("window.history.go(-1)")
        time.sleep(3)
        driver.find_element_by_id('ItemPreview375').click()
        time.sleep(5)
        driver.execute_script("window.history.go(-1)")
        time.sleep(3)
        driver.find_element_by_id('ItemPreview374').click()
        time.sleep(5)

    # раздел ДОКУМЕНТЫ
    def test_08DOC(self):
        driver = self.driver
        driver.find_element_by_partial_link_text('Документы').click()
        time.sleep(3)
        driver.find_element_by_partial_link_text('Законодательство в сфере закупок').click()
        time.sleep(3)
        driver.find_element_by_class_name("col-5").click()
        time.sleep(5)
        driver.find_element_by_class_name("docs-group").click()
        time.sleep(5)
        driver.find_element_by_class_name('col-5').click()
        time.sleep(10)

    # раздел НОВОСТИ
    def test_09NEWS(self):
        driver = self.driver
        driver.find_element_by_id('slick-slide-control00').click()
        time.sleep(2)
        driver.find_element_by_id('slick-slide-control01').click()
        time.sleep(2)
        driver.find_element_by_id('slick-slide-control02').click()
        time.sleep(2)
        driver.find_element_by_id('slick-slide-control03').click()
        time.sleep(2)
        driver.find_element_by_id('slick-slide-control04').click()
        time.sleep(2)
        driver.find_element_by_partial_link_text('Все новости').click()
        time.sleep(20)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
