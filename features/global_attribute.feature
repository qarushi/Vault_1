Feature: Log in and create global attribute

  Scenario: create global attribute
    Given On the log in page
    When Enter username "Gaurav" and account ID "vault" and password "Gaurav@123"
    And Click on the log in button
    Then Redirected to the dashboard page
    And I click on configuration dropdown
    Then I click on global attribute
    And I click on create attribute
    Then I enter attribute name
    And I enter attribute display name
    And Click on entity type dropdown
    Then I select entity type
    And I click on data type dropdown
    And I select data type
    And I click on input type dropdown
    Then I select input field
    And I click on submit
