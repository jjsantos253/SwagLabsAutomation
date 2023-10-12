# Swag Labs Automation test

## Project Description

This automation project is designed to test the functionality of a login page using the Behave BDD (Behavior-Driven Development) framework and Selenium WebDriver. The project simulates various scenarios related to user authentication and error handling on a login page.

## Project Structure

The project contains the following components:

- `features/`: This directory contains Gherkin feature files that define various scenarios to be tested.
- `pages/`: Contains page object classes used to interact with the web application's pages, such as the login page.
- `utilities/`: Houses utility functions, such as JSON data parsing, which are used to support the test automation.
- `resources/`: Contains the test data to be used for the test. This file is being added to avoid hardcoding the credentials and be able to easily replace in the future, but keep in mind that it should not be part of the public project in a real world scenario.


## Installation

1. Clone the repository:

git clone https://github.com/jjsantos2012/SwagLabsAutomation


2. Install the required Python packages using pip:

pip install -r requirements.txt


3. Ensure that you have the Selenium WebDriver executable (e.g., ChromeDriver) installed and available in your system's PATH. You can download the driver from the official Selenium website: [Selenium WebDriver Downloads](https://selenium.dev/documentation/en/webdriver/driver_requirements/)

## Usage

1. Modify the feature files in the `features/` directory to suit your testing needs. Define the scenarios and steps based on your application's requirements.

2. Update the page object classes in the `pages/` directory to reflect the structure and behavior of your web application. The provided code uses a sample login page as an example.

3. Update the `utilities/data_parser.py` file to handle your application's credentials or data sources. The current code reads credentials from a JSON file.

4. To execute the tests, run the following command in your terminal from the project root directory:

behave


This will execute all the feature files and scenarios defined in the `features/` directory.

## Test Scenarios

The project includes various test scenarios to validate different aspects of the login functionality:

- Standard login with valid credentials
- Login with locked-out user credentials
- Login with problem user credentials
- Login with performance user credentials
- Login with error user credentials
- Login with an incorrect password
- Login with an incorrect username
- Testing empty username and valid password
- Testing valid username and an empty password
- Clicking the login button to initiate the login process
- Verifying successful login
- Verifying redirection back to the login page
- Verifying the presence of an error message

## Page Object Class

The `pages/login_page.py` file includes a Page Object class that interacts with the login page elements using Selenium. Here's an explanation of the methods and elements in the class:

- `add_credentials(username, password)`: Enters the provided username and password into the login fields.

- `is_logged_in()`: Checks if the user is successfully logged in by waiting for the appearance of a title element indicating "Products."

- `is_error_message_displayed()`: Checks if an error message is displayed on the page.

- `go_to_login_page()`: Navigates to the login page URL.

- `click_login()`: Clicks the login button.

- `get_error_message()`: Retrieves the text of the error message displayed on the page.

- `is_on_login()`: Checks if the user is on the login page by waiting for the appearance of the login button.

## Reporting

Behave generates test reports in various formats. After running the tests, you can find the reports in the `reports/` directory. You can configure the report format and settings in the `behave.ini` file.

#edited for PR conflict purposes
