Feature: Zen Portal Login Functionality

  Scenario: Successful Login
    Given User launches Zen Portal
    When User enters valid username
    And User enters valid password
    And User clicks login button
    Then User should navigate to dashboard

  Scenario: Unsuccessful Login
    Given User launches Zen Portal
    When User enters invalid username
    And User enters invalid password
    And User clicks login button
    Then User should remain in login page

  Scenario: Validate Username and Password Input Box
    Given User launches Zen Portal
    When User enters username in input field
    And User enters password in input field
    Then Username and Password should be displayed

  Scenario: Validate Submit Button
    Given User launches Zen Portal
    When User enters valid username
    And User enters valid password
    And User clicks login button
    Then Submit button should work properly

  Scenario: Validate Logout Functionality
    Given User launches Zen Portal
    When User enters valid username
    And User enters valid password
    And User clicks login button
    And User clicks logout button
    Then User should navigate back to login page