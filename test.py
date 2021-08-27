from base import BaseFunctions
from selenium import webdriver
from functions import Functions
import unittest


class TestRun(unittest.TestCase, BaseFunctions):
    PARTNER_URL = "https://www.dr.com.tr/kategori/Kitap/Edebiyat/Deneme-Yazin/grupno=00129?Manufacturer[0]=%C4%B0kinci%20Adam%20Yay%C4%B1nlar%C4%B1&ShowNotForSale=True"
    TEXT_FILE = open("/home/ahmet-toktas/Desktop/data.txt", "w")

    def setUp(self):
        self.driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        self.driver.maximize_window()
        self.driver.get(self.PARTNER_URL)
        self.functions = Functions(driver=self.driver)

    def test(self):
        self.TEXT_FILE.write(self.functions.collect_names())
        self.TEXT_FILE.close()

    def TearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
