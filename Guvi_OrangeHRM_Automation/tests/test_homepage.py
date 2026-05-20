#Test-Case-2 : Verify that the home URL is accessible

def test_home_url_accessible(setup):

    driver = setup

    assert "orangehrm" in driver.current_url.lower()