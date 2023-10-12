import requests
import json
from behave import given, when, then

api_key = None


@given('the X-RapidAPI-Key is loaded from "{key_file}"')
def step_given_load_api_key(context, key_file):
    with open(key_file) as api_key_file:
        context.api_key = json.load(api_key_file)["translate-key"]


@given('a request to "{url}"')
def step_given_request_url(context, url):
    context.url = url


@given('the payload is:')
def step_given_payload(context):
    context.payload = json.loads(context.text)


@when('I send a POST request with headers:')
def step_when_send_post_request(context):
    headers = json.loads(context.text)
    response = requests.post(context.url, data=context.payload, headers=headers)
    context.response = response


@then('the response status code should be {status_code}')
def step_then_check_status_code(context, status_code):
    assert context.response.status_code == int(status_code)


@then('the response should contain "{text}"')
def step_then_check_response_contains(context, text):
    assert text in context.response.text
