"""
Test cases for SauceDemo automation
"""

import pytest
from saucedemo_homepage import SauceDemoHome

# Test Data
url = "https://www.saucedemo.com/"


@pytest.fixture
def setup():
    obj = SauceDemoHome(url)
    obj.start_automation()
    yield obj
    obj.shutdown()


# ✅ POSITIVE TEST CASE - Title
def test_positive_title(setup):
    expected_title = "Swag Labs"
    actual_title = setup.fetch_title()
    print(actual_title)
    assert expected_title == actual_title


# ❌ NEGATIVE TEST CASE - Title
def test_negative_title(setup):
    expected_title = "My Store"
    actual_title = setup.fetch_title()
    print(actual_title)
    assert expected_title != actual_title


# ✅ POSITIVE TEST CASE - Homepage URL
def test_positive_homepage_url(setup):
    expected_url = "https://www.saucedemo.com/"
    actual_url = setup.fetch_url()
    print(actual_url)
    assert expected_url == actual_url


# ❌ NEGATIVE TEST CASE - Homepage URL
def test_negative_homepage_url(setup):
    expected_url = "https://www.google.com/"
    actual_url = setup.fetch_url()
    print(actual_url)
    assert expected_url != actual_url


# ✅ LOGIN + DASHBOARD TEST
def test_dashboard_url(setup):
    setup.login()
    dashboard_url = setup.fetch_dashboard_url()
    print(dashboard_url)
    assert "inventory" in dashboard_url


# ✅ SAVE PAGE CONTENT TEST
def test_save_page(setup):
    result = setup.save_page_content()
    assert result == True