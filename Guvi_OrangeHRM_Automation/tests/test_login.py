from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utilities.read_excel import ReadExcel
from utilities.logger import LogGen
from utilities.screenshot import Screenshot


logger = LogGen.loggen()

#Test-Case-1 : Validate login functionality using multiple sets of credentials
def test_login_with_excel_data(setup):

    driver = setup

    file = "C://Users//tamil\PyCharmMiscProject\guviPython\Guvi_OrangeHRM_Automation//testdata\login_data.xlsx"
    sheet = "Sheet1"

    rows = ReadExcel.get_row_count(file, sheet)

    for row in range(2, rows + 1):

        username = ReadExcel.read_data(file, sheet, row, 6)
        password = ReadExcel.read_data(file, sheet, row, 7)

        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)

        logger.info(f"Trying login with username: {username}")

        login_page.login(username, password)

        if dashboard_page.is_dashboard_displayed():
            ReadExcel.write_data(file, sheet, row, 8, "PASS")
            logger.info("Login successful")
            dashboard_page.logout()

        else:
            ReadExcel.write_data(file, sheet, row, 8, "FAIL")
            logger.info("Login failed")
            Screenshot.capture(driver, "login_failed")
            driver.get("https://opensource-demo.orangehrmlive.com/")