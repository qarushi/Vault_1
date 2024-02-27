Feature: log in and create workflow

  Scenario: create workflow
    Given log in page
    Then i enter username "Gaurav" and account ID "vault" and password "Gaurav@123"
    Then  i click on log in button
    When i click on the configration button
    When i click on the regulatory guideline button
    #create new guideline
#    Then i click on create regulatory guideline button
#    And i enter regulatory guideline name
#    And i enter regulatory guideline_description
#    Then i click on submit button
    Then i click on global search bar
    Then i enter input
    Then i right click on Automation workflow 2
    Then i click on edit guideline button
    #first node
    And i click on create node
    Then i enter state name
    And i enter state description
    Then i click submit
    #mark as start node
    And i click on node
    Then i mark it as start node
    And i click on delete button
    #second node
    Then I click for second node
    And I enter second node state
    And I enter description for second node
    Then I click on submit for second node
    #mark as end node
    And I click on second node
    Then I mark it as end node
    And I click on delete button for second node
    #hover on element and connect each other
    When i hover on first node
    Then i compile the guideline