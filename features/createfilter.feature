Feature: log in and create filter


  Scenario: create filter
    Given I on the login page
    When I enter username "Gaurav" and account ID "vault" and password "Gaurav@123"
    And I click on the login button
    Then I should redirected to the dashboard page
    When I click on filter view button
    Then I click on add filter button
    Then I click on add filter to create new filter
    Then I click on field button
    And I select the field status
    Then I click on operator button
    And I select the equal to operator
    Then I click on input text field
    And I entered input Draft
    Then  I click on apply button
    And I enter filter name
    Then I enter description
    And I click on save button