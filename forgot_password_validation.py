from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from yaml_function import YAML_Functions
from excel_functions import Excel_Funtions
from time import sleep

class Forgot_Password_Tests:
    def __init__(self, config_file_name, excel_file_name, sheet_name):
        self.config_file_name = config_file_name
        self.excel_file_name = excel_file_name
        self.sheet = sheet_name
        

    def run(self):
        data = YAML_Functions(self.config_file_name)
        excel_file = Excel_Funtions (self.excel_file_name,self.sheet)
        rows=excel_file.row_count()


        for row in range(2, rows+1):
            username = excel_file.read_data(row, 6)
            test_id = excel_file.read_data(row, 2)
            expected_locator = excel_file.read_data(row,7)

            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
            driver.maximize_window()
            driver.get(data.yaml_reader()['url'])
            driver.implicitly_wait(10)


            driver.find_element(by=By.XPATH, value=data.yaml_reader()['forgot_password_locator']).click()
            sleep(5)

            if driver.find_element(by=By.XPATH, value=data.yaml_reader()['reset_password_title_locator']).is_displayed() == True:
                driver.find_element(by=By.NAME, value=data.yaml_reader()['reset_password_username_locator']).send_keys(username)
                driver.find_element(by=By.XPATH, value=data.yaml_reader()['reset_password_submit_button_locator']).click()
                sleep(5)              
                if driver.find_element(by=By.XPATH, value=expected_locator).is_displayed() == True:
                    print(f"{test_id}- Forgot Password Link Sent Successfully -- TEST PASSED")
                    excel_file.write_data(row, 8, 'Test passed')
                else:           
                    print(f"{test_id}--Forgot Password Link is not Sent -- TEST FAILED")
                    excel_file.write_data(row, 8, 'Test failed')
            else:
                print(" TEST FAILED")
                excel_file.write_data(row, 8, 'Test failed')
            
            driver.quit()