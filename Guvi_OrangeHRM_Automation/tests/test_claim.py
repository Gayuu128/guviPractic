from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.claim_page import ClaimPage

#Test-Case-10 : Initiate a claim request

def test_initiate_claim_request(setup):

    driver = setup

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    claim_page = ClaimPage(driver)

    login_page.login("Admin", "admin123")

    dashboard_page.click_menu("Claim")

    claim_page.click_submit_claim()

    claim_page.select_event()

    claim_page.select_currency()

    claim_page.enter_remarks("Travel expense claim request")

    claim_page.click_create()
    claim_page.final_submit()
    assert claim_page.is_success_message_displayed()
    claim_page.click_back()

