from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import configparser
from selenium.webdriver.chrome.options import Options


class Actions:
    def __init__(self,environment):

        #設定chromedriver 路徑 此範例for mac
        webdriver_chrome_path = '/usr/local/bin/chromedriver'
        options = Options()
        options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(webdriver_chrome_path)

        # 開啟設定檔 config.ini
        ini_file_name = "config.ini"
        self.config = self.getConfig(ini_file_name)

        # 前往  網站
        self.gotoURL(self.config['WEBSITES'][environment])


    def getConfig(self, ini_file_name):
        configuration = configparser.ConfigParser()
        configuration.optionxform = str
        configuration.read(ini_file_name)
        return configuration


    # 移動游標並點擊 Item
    def clickItem(self, xpath):
        # 等待 xpath 出現（這裡假設 xpath 正確）
        WebDriverWait(self.driver, 300).until(lambda driver: driver.find_element_by_xpath(xpath))
        element = self.driver.find_element_by_xpath(xpath)
        #         self.driver.execute_script("arguments[0].click();", element)
        ActionChains(self.driver).move_to_element(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)))).perform()
        ActionChains(self.driver).click().perform()
        sleep(1)

    # 等待 Item 出現
    def waitUntilAppear(self, xpath):
        WebDriverWait(self.driver, 300).until(
            EC.presence_of_element_located((By.XPATH, xpath)))

    # 取得元件的文字敘述
    def getText(self, xpath):
        result =[]
        for item in self.driver.find_elements_by_xpath(xpath):
            result.append(item.text)
        return result
    # 前往頁面 environment = 'qa', ''
    def gotoURL(self, environment):
        environment = self.config['WEBSITES']['environment']
        website = self.config['WEBSITES'][environment]
        self.driver.get(website)
