from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from yaml_function import YAML_Functions
from excel_functions import Excel_Funtions
from time import sleep


class Main_Menu_Validation_Tests:
    def __init__(self, config_file_name, excel_file_name, sheet_name):
        self.config_file_name = config_file_name
        self.excel_file_name = excel_file_name
        self.sheet = sheet_name
        

    def run(self):
        data = YAML_Functions(self.config_file_name)
        excel_file = Excel_Funtions (self.excel_file_name,self.sheet)
        rows=excel_file.row_count()

        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get(data.yaml_reader()['url'])
        driver.implicitly_wait(10)

        driver.find_element(by=By.NAME, value=data.yaml_reader()['username_locator']).send_keys(data.yaml_reader()['username'])
        driver.find_element(by=By.NAME, value=data.yaml_reader()['password_locator']).send_keys(data.yaml_reader()['password'])
        driver.find_element(by=By.XPATH, value=data.yaml_reader()['login_button_locator']).click()
        sleep(8)

        for row in range(2, rows+1):
            menu_text = excel_file.read_data(row, 6)
            locators_value = excel_file.read_data(row, 7)
            test_id = excel_file.read_data(row, 2)


            if driver.find_element(by=By.XPATH, value=locators_value).is_displayed() == True:
                print(f"{test_id}--{menu_text} menu is visible- TEST PASSED")
                excel_file.write_data(row, 8, 'Test passed')
            else:            
                print(f"{test_id}--{menu_text} menu is not visible- TEST FAILED")
                excel_file.write_data(row, 8, 'Test failed')
        
     


        driver.quit()