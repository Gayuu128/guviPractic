from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage

#Test-Case-6 : Validate presence of the newly created user in admin list
def test_search_user_in_admin(setup):

    driver = setup

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    admin_page = AdminPage(driver)

    login_page.login("Admin", "admin123")

    dashboard_page.click_menu("Admin")

    admin_page.search_user("Admin")

    assert admin_page.is_user_found()

    dashboard_page.logout()