  Feature: Validate the login feature

  Background:
    Given Open the website
    When The login portal has been opened

  @valid_login
  Scenario: Login with valid credentials
    Then Provide the username "Gaurav", account id "vault" and password "Gaurav@123"
    Then Click on the Login button
    Then Login is successful and dashboard is opened
    Then Dashboard Screenshot should be captured
    Then Verify user should be able to logout
    # Then Close the browser
  @invalid_login
  Scenario: Login with invalid credentials
    Then Provide the username "TestUser", account id "vault" and password "Teset@123"
    Then Click on the Login button
    Then Login is failed and invalid credential error message "Username does not exist." is displayed
    Then Screenshot of Error Message should be captured

    # Then Screenshot of Error Message should be captured
    # Then Close the browser

  Scenario: Login with empty username
    Then Provide the account id "vault" and password "Gaurav@123"
    Then Click on the Login button
    Then Login is failed and empty username error is displayed

    # Then Close the browser

  Scenario: Login with empty password
    Then Provide the username "Gaurav" and account id "vault"
    Then Click on the Login button
    Then Login is failed and empty password error is displayed

  Scenario: Login with empty account id
    Then Provide the username "Gaurav" and passowrd "Gaurav@123"
    Then Click on the Login button
    Then Login is failed and empty account id error is displayed


  Scenario: Close the browser
  Then Close the browser  


  