Feature: Login

  Scenario: Successful login (standard)
    Given I am on the login page
    When I enter standard credentials
    And I click the login button
    Then I should be logged in

  Scenario: Unsuccessful login (locked out user)
    Given I am on the login page
    When I enter locked user credentials
    And I click the login button
    Then I should see the error message 'Epic sadface: Sorry, this user has been locked out.'


  Scenario: Successful login (problem)
    Given I am on the login page
    When I enter problem user credentials
    And I click the login button
    Then I should be logged in

  Scenario: Successful login (performance)
    Given I am on the login page
    When I enter performance user credentials
    And I click the login button
    Then I should be logged in

  Scenario: Successful login (error user)
    Given I am on the login page
    When I enter error user credentials
    And I click the login button
    Then I should be logged in

  Scenario: Unsuccessful login (incorrect password)
    Given I am on the login page
    When I enter incorrect password
    And I click the login button
    Then I should see the error message 'Epic sadface: Username and password do not match any user in this service'

  Scenario: Unsuccessful login (incorrect username)
    Given I am on the login page
    When I enter incorrect username
    And I click the login button
    Then I should see the error message 'Epic sadface: Username and password do not match any user in this service'

  Scenario: Unsuccessful login (empty fields)
    Given I am on the login page
    When I click the login button
    Then I should see the error message 'Epic sadface: Username is required'

  Scenario: Unsuccessful login (empty username)
    Given I am on the login page
    When I enter an valid password and empty username
    And I click the login button
    Then I should see the error message 'Epic sadface: Username is required'

  Scenario: Unsuccessful login (empty password)
    Given I am on the login page
    When I enter a valid username and empty password
    And I click the login button
    Then I should see the error message 'Epic sadface: Password is required'