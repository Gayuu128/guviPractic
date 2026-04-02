import pytest
from login_excel import LoginPage, ExcelUtils

file_path = "C:/Users/tamil/PyCharmMiscProject/guviPython/PAT_Task_15/test_data.xlsx"

@pytest.mark.parametrize("row", range(2, 7))
def test_login_ddtf(setup, row):

    driver = setup
    login = LoginPage(driver)
    excel = ExcelUtils(file_path)

    username = excel.get_data(row, 2)
    password = excel.get_data(row, 3)

    login.login(username, password)

    if login.is_login_success():
        excel.write_result(row, "Pass")
        assert True
    else:
        excel.write_result(row, "Fail")
        assert False