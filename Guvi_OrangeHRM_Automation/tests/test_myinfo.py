from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.myinfo_page import MyInfoPage

#Test-Case-8 : Validate menu items under My Info

def test_myinfo_submenu_items(setup):

    driver = setup

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    myinfo_page = MyInfoPage(driver)

    login_page.login("Admin", "admin123")

    dashboard_page.click_menu("My Info")

    submenus = [
        "Personal Details",
        "Contact Details",
        "Emergency Contacts",
        "Dependents",
        "Immigration",
        "Job",
        "Salary"
    ]

    for submenu in submenus:
        assert myinfo_page.is_submenu_clickable(submenu)

    dashboard_page.logout()