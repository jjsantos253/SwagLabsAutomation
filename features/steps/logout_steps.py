from behave import given, when, then
from selenium import webdriver
from pages.base_page import BasePage


@then("I open the side menu")
def step_given_login_page(context):
    context.base_page = BasePage(context.driver)
    context.base_page.click_side_menu()


@then("I click on logout")
def step_given_login_page(context):
    context.base_page = BasePage(context.driver)
    context.base_page.click_logout()