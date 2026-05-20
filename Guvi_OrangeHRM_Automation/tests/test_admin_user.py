

from pages.admin_user_page import  AdminUserPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

#Test-Case-5 : Create a new user and validate login
def test_create_new_user_and_validate_login(setup):
    driver = setup

    login_page = LoginPage(driver)
    admin_page = AdminUserPage(driver)
    dashboard_page = DashboardPage(driver)

    new_username = "testuser123"
    new_password = "Test@12345"

    # Login as Admin
    login_page.login("Admin", "admin123")

    # Navigate to Admin menu
    admin_page.click_admin_menu()

    # Add new user
    admin_page.click_add_button()
    admin_page.select_user_role("ESS")
    admin_page.enter_employee_name("a")
    admin_page.select_employee_suggestion()
    admin_page.select_status("Enabled")
    admin_page.enter_username(new_username)
    admin_page.enter_password(new_password)
    admin_page.enter_confirm_password(new_password)
    admin_page.click_save()

    dashboard_page.logout()

    login_page.login(new_username, new_password)

    assert "login" in driver.current_url