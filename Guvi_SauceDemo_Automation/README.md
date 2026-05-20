# SauceDemo Automation Testing Project

## Project Objective

This project automates the testing of the SauceDemo e-commerce web application using Selenium WebDriver, Python, Pytest, and Page Object Model.

Application URL: https://www.saucedemo.com/

## Tools Used

- Python
- Selenium WebDriver
- Pytest
- Pytest HTML Report
- Allure Report
- WebDriver Manager
- Chrome Browser

## Framework Design

This project follows Page Object Model.

## Folder Structure

- pages: Contains page classes and locators
- tests: Contains test case files
- screenshots: Stores screenshots
- reports: Stores allure reports
- conftest.py: Browser setup and teardown
- pytest.ini: Pytest configuration

## Test Cases Covered

1. Login with predefined users
2. Login with invalid credentials
3. Validate logout functionality
4. Check cart icon visibility
5. Random product selection and data extraction
6. Add selected products to cart
7. Validate cart product details
8. Complete checkout and validate order
9. Validate sorting functionality
10. Validate Reset App State functionality

## Installation

```bash
pip install -r requirements.txt