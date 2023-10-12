Feature: Automate API Requests

  Background:
    Given the X-RapidAPI-Key is loaded from "resources/api_key.json"

  Scenario: Detect Language
    Given a request to "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"
    And the payload is:
      """
      {
        "q": "English is hard, but detectably so"
      }
      """
    When I send a POST request with headers:
      """
      {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
      }
      """
    Then the response status code should be 200
    And the response should contain "language"

