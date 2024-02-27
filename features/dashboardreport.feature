Feature: log in and view dashboard report


  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter my username "Gaurav" and account ID "vault" and password "Gaurav@123"
    And I click the login button
    Then I should be redirected to the dashboard page
    And I take a screenshot of the dashboard

  Scenario: view report
    When I click on the report button
    Then I should directed to report
    And I take a screenshot of the report