from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage
from utilities.data_parser import parse_json_credentials


@given("I am on the login page")
def step_given_login_page(context):
    context.driver = webdriver.Chrome()
    context.login_page = LoginPage(context.driver)
    context.login_page.go_to_login_page()


@when("I enter standard credentials")
def step_when_enter_valid_credentials(context):
    credentials = parse_json_credentials("resources/login_credentials.json")
    context.login_page.add_credentials(credentials["username-standard"], credentials["password"])


@when("I enter locked user credentials")
def step_when_enter_valid_credentials(context):
    credentials = parse_json_credentials("resources/login_credentials.json")
    context.login_page.add_credentials(credentials["username-locked-out"], credentials["password"])


@when("I enter problem user credentials")
def step_when_enter_valid_credentials(context):
    credentials = parse_json_credentials("resources/login_credentials.json")
    context.login_page.add_credentials(credentials["username-problem"], credentials["password"])


@when("I enter performance user credentials")
def step_when_enter_valid_credentials(context):
    credentials = parse_json_credentials("resources/login_credentials.json")
    context.login_page.add_credentials(credentials["username-performance"], credentials["password"])


@when("I enter error user credentials")
def step_when_enter_valid_credentials(context):
    credentials = parse_json_credentials("resources/login_credentials.json")
    context.login_page.add_credentials(credentials["username-error"], credentials["password"])


@when("I enter incorrect password")
def step_when_enter_invalid_password(context):
    credentials = parse_json_credentials("resources/login_credentials.json")
    context.login_page.add_credentials(credentials["username-standard"], "test1")


@when("I enter incorrect username")
def step_when_enter_invalid_username(context):
    credentials = parse_json_credentials("resources/login_credentials.json")
    context.login_page.add_credentials("test1", credentials["password"])


@then("I should see the error message {expected_message}")
def step_then_i_should_see_error_message(context, expected_message):
    actual_message = context.login_page.get_error_message()
    actual_message = "'" + actual_message + "'"
    assert actual_message == expected_message, f"Expected message: {expected_message}, but got: '{actual_message}'"


@when("I enter an valid password and empty username")
def step_when_enter_empty_username(context):
    credentials = parse_json_credentials("resources/login_credentials.json")
    context.login_page.add_credentials("", credentials["password"])


@when("I enter a valid username and empty password")
def step_when_enter_empty_password(context):
    credentials = parse_json_credentials("resources/login_credentials.json")
    context.login_page.add_credentials(credentials["username-standard"], "")


@when("I click the login button")
def step_when_click_login_button(context):
    context.login_page.click_login()


@then("I should be logged in")
def step_then_logged_in(context):
    assert context.login_page.is_logged_in()


@then("I am on the login page again")
def step_then_logged_in(context):
    assert context.login_page.is_on_login()


@then("I should see an error message")
def step_then_error_message(context):
    assert context.login_page.is_error_message_displayed()
