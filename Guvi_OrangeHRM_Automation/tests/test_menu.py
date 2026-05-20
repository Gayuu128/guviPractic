from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

#Test-Case-4 : Verify visibility and clickability of main menu items after login
def test_main_menu_items(setup):

    driver = setup

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    login_page.login("Admin", "admin123")

    menu_list = [
        "Admin",
        "PIM",
        "Leave",
        "Time",
        "Recruitment",
        "My Info",
        "Performance",
        "Dashboard"
    ]

    for menu in menu_list:
        assert dashboard_page.is_menu_visible_and_clickable(menu)

    dashboard_page.logout()