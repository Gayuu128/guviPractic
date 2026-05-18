# GUVI Automation Testing using Playwright + Python

## Project Overview

This project automates testing of GUVI website using:

- Python
- Playwright
- Pytest
- POM design pattern
- OOP principles

## Features

- Positive and negative testing
- Logging
- HTML reports
- Screenshot capture on failures
- Exception handling

## Framework Architecture

POM Architecture:

Tests
↓
Pages
↓
BasePage
↓
Playwright

## Execute

pytest -v

Generate reports:

pytest --html=reports/report.html