from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.leave_page import LeavePage

#Test-Case-9 : Assign leave to an employee
def test_assign_leave(setup):

    driver = setup

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    leave_page = LeavePage(driver)

    login_page.login("Admin", "admin123")

    dashboard_page.click_menu("Leave")
    leave_page.click_assign_leave()
    leave_page.enter_employee_name("a")
    leave_page.select_leave_type()
    leave_page.select_dates()
    leave_page.click_assign()
    dashboard_page.logout()