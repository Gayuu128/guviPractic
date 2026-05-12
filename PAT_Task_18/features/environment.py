from playwright.sync_api import sync_playwright


def before_scenario(context, scenario):

    playwright = sync_playwright().start()

    browser = playwright.chromium.launch(
        headless=False,
        slow_mo=1000
    )

    context.browser = browser

    context.page = browser.new_page()

    # Open Zen Portal
    context.page.goto(
        "https://www.zenclass.in/login",
        wait_until="networkidle"
    )

    # Extra wait for React rendering
    context.page.wait_for_timeout(5000)

    context.playwright = playwright


def after_scenario(context, scenario):

    context.browser.close()

    context.playwright.stop()