from behave import *
from pages.zen_login_page import ZenLoginPage


@given("User launches Zen Portal")
def launch_portal(context):

    context.page.goto(
        "https://www.zenclass.in/login"
    )

    context.login = ZenLoginPage(
        context.page
    )


@when("User enters valid username")
def enter_valid_username(context):

    context.login.enter_username(
        "valid_email"
    )


@when("User enters valid password")
def enter_valid_password(context):

    context.login.enter_password(
        "valid_password"
    )


@when("User enters invalid username")
def enter_invalid_username(context):

    context.login.enter_username(
        "invalid_user"
    )


@when("User enters invalid password")
def enter_invalid_password(context):

    context.login.enter_password(
        "invalid_password"
    )


@when("User clicks login button")
def click_login(context):

    context.login.click_login()


@then("User should navigate to dashboard")
def validate_dashboard(context):

    assert context.login.is_login_successful()


@then("User should remain in login page")
def validate_login_page(context):

    assert "login" in context.page.url.lower()


@when("User enters username in input field")
def validate_username_input(context):

    context.login.enter_username(
        "valid_email"
    )


@when("User enters password in input field")
def validate_password_input(context):

    context.login.enter_password(
        "valid_password"
    )


@then("Username and Password should be displayed")
def validate_input_fields(context):

    username_value = context.page.locator(
        context.login.username_input
    ).input_value()

    password_value = context.page.locator(
        context.login.password_input
    ).input_value()

    assert username_value == "valid_email"

    assert password_value == "valid_password"


@then("Submit button should work properly")
def validate_submit_button(context):

    assert "dashboard" in context.page.url.lower()


@when("User clicks logout button")
def click_logout(context):

    context.login.open_profile_menu()

    context.login.click_logout()


@then("User should navigate back to login page")
def validate_logout(context):

    context.page.wait_for_url(
        "**/login",
        timeout=30000
    )

    assert "login" in context.page.url.lower()