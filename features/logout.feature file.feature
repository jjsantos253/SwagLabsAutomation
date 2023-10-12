Feature: Logout

  Scenario: Logout for standard user
    Given I am on the login page
    When I enter standard credentials
    And I click the login button
    Then I should be logged in
    Then I open the side menu
    And I click on logout
    Then I am on the login page again

  Scenario: Logout for problem user
    Given I am on the login page
    When I enter problem user credentials
    And I click the login button
    Then I should be logged in
    Then I open the side menu
    And I click on logout
    Then I am on the login page again

  Scenario: Logout for performance user
    Given I am on the login page
    When I enter performance user credentials
    And I click the login button
    Then I should be logged in
    Then I open the side menu
    And I click on logout
    Then I am on the login page again

  Scenario: Logout for error user
    Given I am on the login page
    When I enter error user credentials
    And I click the login button
    Then I open the side menu
    And I click on logout
    Then I am on the login page again