from header_validation import Header_Validation_Tests
from main_menu_validation import Main_Menu_Validation_Tests


config_yaml_file_name = 'D:\Meena\orange-hrm-tests-2\config.yaml'
excel_file_name = 'D:\Meena\orange-hrm-tests-2\Testcase_data.xlsx'
header_sheet_name = 'Header Validation'
menu_sheet_name = 'Main Menu Validation'


header_validation = Header_Validation_Tests(config_yaml_file_name,excel_file_name,header_sheet_name)
header_validation.run()

main_menu_validation = Main_Menu_Validation_Tests(config_yaml_file_name,excel_file_name, menu_sheet_name)
main_menu_validation.run()



